#!/usr/bin/env /usr/local/opt/anaconda/bin/python

# import scipy as sp
import numpy as np
import scipy.constants as spc
import matplotlib.pyplot as plt
plt.style.use('messiah')

dz0,dt0,ipk0 = np.loadtxt('../../dat/curr_init.dat',unpack=True)
dz1,dt1,ipk1 = np.loadtxt('../../dat/ltu1/current.dat', unpack=True)
# dz2,dt2,ipk2 = np.loadtxt('../../1011/dat/current.dat', unpack=True)

fig6   = plt.figure();
ax6 = fig6.add_axes([0.110, 0.140, 0.840, 0.760])
ax6.set_title('Current Profile of LTU-1',fontstyle='italic')
im0 = ax6.plot(dz0*spc.mega,ipk0/spc.kilo,lw=5.0,c=(0.7,0.8,0))
im1 = ax6.plot(dz1*spc.mega,ipk1/spc.kilo,lw=1.0,c='r')
ax6.set_xlabel(r'$z\ (\mu m)$')
ax6.set_ylabel(r'$I_{pk}\ (kA)$')
ax6.set_xlim([min(dz0*spc.mega)-2,max(dz0*spc.mega)+2])
# im2 = ax6.plot(dz2*spc.kilo,ipk2/spc.kilo,lw=1.0,c='b')
ax6.ticklabel_format(style='plain',axis='y')
#ax6.set_yticks([0.0, 1.0, 2.0, 3.0, 4.0])
#ax6.set_yticklabels(('0.0', '1.0', '2.0', '3.0', '4.0'))
plt.legend(im0+im1,['Initial','final'],ncol=1)


plt.show()

# fig6.savefig('../../fig/ltu1/ipk.png')
