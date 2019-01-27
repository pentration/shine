#!/usr/bin/env /usr/local/opt/anaconda/bin/python

import numpy as np
import scipy as sp
import math
import scipy.constants as spc
import string
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('messiah')

s1,betax,yy,cy,cyy,betay,etax,etay,etaxp,etayp = np.loadtxt('../dat/kick/kick.dat',usecols=(0,2,3,4,5,6,7,8,9,10),unpack=True,skiprows=2)
s2,prof = np.loadtxt('../dat/kick/prof.dat',unpack=True)


dy0 = 1.651943136e+01
# print(etax[len(cyy)-1],etaxp[len(cyy)-1],etay[len(cyy)-1],etayp[len(cyy)-1])
# print(cyy[len(cyy)-1]-cyy[len(cyy)-2])

fig1   = plt.figure()
ax1 = fig1.add_axes([0.110, 0.140, 0.690, 0.710])
l1 = ax1.plot(s1,betax)
l2 = ax1.plot(s1,betay)
ax1.set_title(r'$\beta$-functions and dispersions of K2S section',fontstyle='italic')
ax1.ticklabel_format(style='sci',axis='both')
ax1.set_xlim([s1[0]-2,s1[-1]+2])
ax1.set_ylim([min(min(betax),min(betay))-1,max(max(betax),max(betay))+3])
ax1.set_xlabel(r'$s\ (m)$')
ax1.set_ylabel(r'$\beta_{x,y}\ ({m})$')
ax11= ax1.twinx()
l4 = ax11.plot(s1,etax,'r-.',ms=0.4)
l5 = ax11.plot(s1,etay,'y-.',ms=0.4)
ax11.set_ylim([min(min(etax),min(etay))*1.05-0.001,max(max(etax),max(etay))*1.1])
ax11.set_ylabel(r'$\eta_{x,y}\ (m)$',fontsize='x-large')
ax12=ax1.twinx()
ax12.yaxis.set_ticks_position('right')
ax12.spines['right'].set_position(('data', ax1.get_xlim()[1]*1.14-ax1.get_xlim()[0]*0.14))
ax12.set_ylim([-18,2])
l3 = ax12.plot(s1,cyy*spc.kilo,'k--')
ax12.set_ylim([min(cyy)*spc.kilo-2,max(cyy)*spc.kilo+4])
ax12.set_ylabel(r'$\Delta{y}\ (mm)$',fontsize='x-large')
plt.legend(l1+l2+l3+l4+l5,[r'$\beta_{x}$',r'$\beta_{y}$',r'$\Delta{y}$',r'$\eta_x$',r'$\eta_y$'],ncol=5)
ax10 = fig1.add_axes([0.110, 0.930, 0.690, 0.030])
ax10.plot(s2,prof,c='k',lw=0.4) 
ax10.set_xlim(ax1.get_xlim())
ax10.set_xticks([])
ax10.set_yticks([])
ax10.spines['right'].set_color('none')
ax10.spines['top'].set_color('none')
ax10.spines['bottom'].set_color('none')
ax10.spines['left'].set_color('none')

plt.show()
# fig1.savefig('../fig/kick/beta.eps')


