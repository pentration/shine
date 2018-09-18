#!/usr/bin/env /usr/local/opt/anaconda/bin/python

# import scipy as sp
import numpy as np
import scipy.constants as spc
import string
import matplotlib.pyplot as plt
#import matplotlib.pylab as pl
import enhancePlot as ep
import matplotlib
# import re
plt.style.use('messiah')

# os.system('./run/runScript')

t,p = np.loadtxt('../../dat/ltu3/lhoff/t-p0.dat',usecols=(0,1),unpack=True,skiprows=0)
dz,ipk = np.loadtxt('../../dat/ltu3/lhoff/current0.dat',usecols=(0,2),unpack=True,skiprows=0)

dz=dz*spc.mega
ipk=ipk/spc.kilo

print("LOAD COMPLETE")


h_grid = 1000
v_grid = 500

[t_mean,p_mean]=[np.mean(t),np.mean(p)]
ct=t
dp=p

for i in range(len(ct)):
    ct[i]=(t_mean-t[i])*spc.c*spc.mega
    dp[i]=(p[i]-p_mean)/p_mean*spc.kilo

[ct_max,ct_min]=[np.max(ct),np.min(ct)]
[dp_max,dp_min]=[np.max(dp),np.min(dp)]

dct = 1.01*(ct_max-ct_min)/(h_grid-1)
ddp = 1.01*(dp_max-dp_min)/(v_grid-1)
s = np.linspace(ct_min-0.01*dct,ct_max+0.01*dct,h_grid)
g = np.linspace(dp_min-0.01*ddp,dp_max+0.01*ddp,v_grid)

tp = [0]*v_grid
for i in range(v_grid):
    tp[i]=[0]*h_grid

# print tp
for i in range(len(ct)):
    s1=int(round((ct[i]-ct_min+0.01*dct)/dct))
    g1=int(round((dp[i]-dp_min+0.01*ddp)/ddp))
    tp[g1][s1]=tp[g1][s1]+1
    # ct[i]=(ct_mean-ct[i])*spc.kilo

fig0   = plt.figure(figsize=(8,5),dpi=100,facecolor='white');
ax0 = fig0.add_axes([0.15, 0.20, 0.70, 0.70])
plt1 = ep.enhancePlot(title="t-p phase space with laser-heater off")
# cmap = matplotlib.cm.binary
# cmap = matplotlib.cm.inferno
# cmap = matplotlib.cm.magma
cmap = matplotlib.cm.jet
ax0.contourf(s,g,tp,cmap=cmap)
plt1.eSetPlot(ax0,axis=[r'$ct\ ({\mu}m)$',r'$\Delta{p}/p\ (\perthousand)$'])
ax01=ax0.twinx()
plt1.ePlot(ax01,dz,ipk,mt='-',cl='r',lw=1.5,pltLabel=[r'$I_{pk}$'])
# plt1.eSetPlot(ax01)
ax01.set_ylabel(r'$I_{pk}\ (kA)$',fontsize='xx-large')
ax01.set_xlim([ct_min,ct_max])
ax01.set_ylim([0,np.max(ipk)*1.1])
# ax6.legend(l1,[r'End of Linac',r'End of LTU3'],bbox_to_anchor=(0.50,1.10),ncol=2)
ax01.legend(loc='upper center',bbox_to_anchor=(0.90,1.12),frameon=False,fontsize='large')
plt.yticks(fontsize='large')

plt.show()
fig0.savefig('../../fig/ltu3/t-p0.eps')


