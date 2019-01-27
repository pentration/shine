#!/usr/bin/env /usr/local/opt/anaconda/bin/python

# import scipy as sp
import numpy as np
import scipy.constants as spc
import string
import matplotlib as mpl
import matplotlib.pyplot as plt
import countFreq

plt.style.use('messiah')


tpDistribution = '../../dat/ltu3/t-p.bin'
currentProfile = '../../dat/ltu3/current.dat'
nParticle = np.loadtxt('../../dat/ltu3/nParticle.dat',unpack=True)
tp = np.fromfile(open(tpDistribution)).reshape(int(nParticle),2).T
dz,dt,ipk = np.loadtxt(currentProfile,unpack=True)

p_mean = np.mean(tp[1])

print("LOAD COMPLETE")

h_grid = 500
v_grid = 300

s,g,freq = countFreq.countFreq(tp[0],tp[1],h_grid,v_grid)

print("COUNT COMPLETE")

fig0   = plt.figure();
ax0 = fig0.add_axes([0.110, 0.140, 0.700, 0.760])
gci = ax0.contourf(-s*spc.c*spc.mega,g/p_mean*spc.kilo,freq)
ax0.set_xlim([min(-s*spc.c*spc.mega),max(-s*spc.c*spc.mega)])
position = fig0.add_axes([0.910, 0.140, 0.03, 0.760])
cb=plt.colorbar(gci,cax=position,orientation='vertical',extendfrac='auto')
ax0.set_title(r'Longitudinal Phase Space - LTU1',fontstyle='italic')
ax0.set_xlabel(r'$z\ (\mu m)$')
ax0.set_ylabel(r'$\Delta{p}/p\ (\perthousand)$')
ax01=ax0.twinx()
ax01.plot(dz*spc.mega,ipk/spc.kilo,'-',c='r',lw=1.0)
ax01.set_ylabel(r'$I_{pk}\ (kA)$')
ax01.set_xlim([ax0.get_xlim()[0],ax0.get_xlim()[1]])
ax01.ticklabel_format(style='plain',axis='y')

plt.show()
# fig0.savefig('../../fig/ltu3/t-p.png')

