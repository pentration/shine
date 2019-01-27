#!/usr/bin/env /usr/local/opt/anaconda/bin/python

import numpy as np
import math
import scipy.constants as spc
import string
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('messiah')

s1,betax1,yy1,cy1,cyy1,betay1,etax1,etay1,etaxp1,etayp1 = np.loadtxt('../dat/kick/kick.dat',usecols=(0,2,3,4,5,6,7,8,9,10),unpack=True,skiprows=2)
s3,prof3 = np.loadtxt('../dat/kick/prof.dat',unpack=True)
s2,betax2,yy2,cy2,cyy2,betay2,etax2,etay2,etaxp2,etayp2 = np.loadtxt('../dat/ltu0/param.dat',usecols=(0,2,3,4,5,6,7,8,9,10),unpack=True,skiprows=2)
s4,prof4 = np.loadtxt('../dat/ltu0/prof.dat',unpack=True)

s1max = s1[-1]
dy0 = cyy1[-1]

s2 = s2+s1max
s4 = s4+s1max
s5 = np.append(s1,s2)
s6 = np.append(s3,s4)

betax = np.append(betax1,betax2)
betay = np.append(betay1,betay2)
etax = np.append(etax1,etax2)
etay = np.append(etay1,etay2)
cyy = np.append(cyy1,cyy2+dy0)
prof = np.append(prof3,prof4)

fig1   = plt.figure()
ax1 = fig1.add_axes([0.110, 0.140, 0.690, 0.710])
l1 = ax1.plot(s5,betax,label=r'$\beta_{x}$')
l2 = ax1.plot(s5,betay,label=r'$\beta_{y}$')
ax1.set_title(r'$\beta$-functions and dispersions of LTU-3',fontstyle='italic')
ax1.set_xlim([s5[0]-5,s5[-1]+5])
ax1.set_ylim([min(min(betax),min(betay))-2,max(max(betax),max(betay))+2])
ax1.ticklabel_format(style='plain',axis='x')
ax1.set_xlabel(r'$s\ (m)$')
ax1.set_ylabel(r'$\beta_{x,y}\ ({m})$')

ax11= ax1.twinx()
l4 = ax11.plot(s5,etax,'r-.',ms=0.4,label=r'$\eta_{x}$')
l5 = ax11.plot(s5,etay,'y-.',ms=0.4,label=r'$\eta_{y}$')
ax11.set_ylim([min(min(etax),min(etay))*1.05,max(max(etax),max(etay))*1.05])
ax11.set_ylabel(r'$\eta_{x,y}\ (m)$')

ax12=ax1.twinx()
ax12.yaxis.set_ticks_position('right')
ax12.spines['right'].set_position(('data', ax1.get_xlim()[1]*1.14-ax1.get_xlim()[0]*0.14))
l3 = ax12.plot(s5,cyy*spc.kilo,'k--',ms=0.5,label=r'$\Delta{y}$')
ax12.set_ylim([min(cyy)*spc.kilo-5,max(cyy)*spc.kilo+15])
ax12.set_ylabel(r'$\Delta{y}\ (mm)$')
plt.legend(l1+l2+l3+l4+l5,[r'$\beta_{x}$',r'$\beta_{y}$',r'$\Delta{y}$',r'$\eta_{x}$',r'$\eta_{y}$'],loc='upper right',ncol=2)

ax10 = fig1.add_axes([0.110, 0.930, 0.690, 0.030])
ax10.plot(s6,prof,c='k',lw=0.4)
ax10.set_xlim(ax1.get_xlim())
ax10.set_xticks([])
ax10.set_yticks([])
ax10.spines['right'].set_color('none')
ax10.spines['top'].set_color('none')
ax10.spines['bottom'].set_color('none')
ax10.spines['left'].set_color('none')

plt.show()
# fig1.savefig('../fig/kick/beta.eps')


