#!/usr/bin/env /usr/local/opt/anaconda/bin/python

# import scipy as sp
import numpy as np
import scipy.constants as spc
import string
import matplotlib as mpl
import matplotlib.pyplot as plt
import enhancePlot as ep
import countFreq

plt.style.use('messiah')

# os.system('./run/runScript')

tpDistribution = '../../dat/ltu2/t-p.bin'
currentProfile = '../../dat/ltu2/current.dat'
nParticle = np.loadtxt('../../dat/ltu2/nParticle.dat',unpack=True)
tp = np.fromfile(open(tpDistribution)).reshape(int(nParticle),2).T
dz,dt,ipk = np.loadtxt(currentProfile,unpack=True)

p_mean = np.mean(tp[1])

print("LOAD COMPLETE")

h_grid = 500
v_grid = 300

s,g,freq = countFreq.countFreq(tp[0],tp[1],h_grid,v_grid)

print("COUNT COMPLETE")

fig0   = plt.figure(facecolor='white');
ax0 = fig0.add_axes([0.12, 0.20, 0.68, 0.70])
plt1 = ep.enhancePlot(mt='o',ms=0.1,title='Longitudinal Phase Space - LTU2')
gci = ax0.contourf(-s*spc.c*spc.mega,g/p_mean*spc.kilo,freq)
plt1.eSetPlot(ax0,axis=[r'$z\ (\mu m)$',r'$\Delta{p}/p\ (\perthousand)$'])
position = fig0.add_axes([0.90, 0.20, 0.03, 0.70])
cb=plt.colorbar(gci,cax=position,orientation='vertical')
ax01=ax0.twinx()
ax01.plot(dz*spc.mega,ipk/spc.kilo,'-',c='r',lw=1.0)
plt1.eSetPlot(ax01)
ax01.set_ylabel(r'$I_{pk}\ (kA)$')
ax01.set_xlim([ax0.get_xlim()[0],ax0.get_xlim()[1]])
ax01.ticklabel_format(style='plain',axis='y')

plt.show()
fig0.savefig('../../fig/ltu2/t-p.png')

