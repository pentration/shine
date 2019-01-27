#!/usr/bin/env /usr/local/opt/anaconda/bin/python

# import scipy as sp
import numpy as np
import scipy.constants as spc
import matplotlib.pyplot as plt
plt.style.use('messiah')

dz0,dt0,ipk0 = np.loadtxt('../dat/curr_init.dat',unpack=True)
dz1,dt1,ipk1 = np.loadtxt('../dat/ltu1/current.dat', unpack=True)
dz2,dt2,ipk2 = np.loadtxt('../dat/ltu2/current.dat', unpack=True)
dz3,dt3,ipk3 = np.loadtxt('../dat/ltu3/current.dat',unpack=True)

fig6   = plt.figure();
ax6 = fig6.add_axes([0.15, 0.20, 0.75, 0.70])
im0 = ax6.plot(dz0*spc.mega,ipk0/spc.kilo,lw=5.0,c=(0.7,0.8,0))
im1 = ax6.plot(dz1*spc.mega,ipk1/spc.kilo,lw=1.0,c='r')
im2 = ax6.plot(dz2*spc.mega,ipk2/spc.kilo,lw=1.0,c='b')
im3 = ax6.plot(dz3*spc.mega,ipk3/spc.kilo,lw=1.0,c='k')
ax6.set_title(r'Comparison of Current Profile',fontstyle='italic')
ax6.set_xlabel(r'$ct\ (\mu m)$')
ax6.set_ylabel(r'$I_{pk}\ (kA)$'])
ax6.ticklabel_format(style='plain',axis='y')
#ax6.set_yticks([0.0, 1.0, 2.0, 3.0, 4.0])
#ax6.set_yticklabels(('0.0', '1.0', '2.0', '3.0', '4.0'))
plt.legend(im0+im1+im2+im3,['Initial','LTU-1','LTU-2','LTU-3'],bbox_to_anchor=(0.50,1.015),ncol=2)

# fig6.savefig('../fig/ipk-comp.png')

plt.show()
