#!/usr/bin/env /usr/local/opt/anaconda/bin/python

import numpy as np
import scipy as sp
import math
import scipy.constants as spc
import string
import matplotlib as mpl
import matplotlib.pyplot as plt
import enhancePlot as ep

plt.style.use('messiah')

s1,betax,yy,cy,cyy,betay,etax,etay,etaxp,etayp = np.loadtxt('../dat/kick/kick.dat',usecols=(0,2,3,4,5,6,7,8,9,10),unpack=True,skiprows=2)
s2,prof = np.loadtxt('../dat/kick/prof.dat',unpack=True)

# print(etax[len(cyy)-1],etaxp[len(cyy)-1],etay[len(cyy)-1],etayp[len(cyy)-1])
# print(cyy[len(cyy)-1]-cyy[len(cyy)-2])

fig1   = plt.figure()
ax1 = fig1.add_axes([0.15, 0.20, 0.65, 0.60])
plt1 = ep.enhancePlot(title=r'Optics of the Kicker-Septum')
l1 = ax1.plot(s1,betax)
l2 = ax1.plot(s1,betay)
plt1.eSetPlot(ax1)
ax1.ticklabel_format(style='plain',axis='y')
ax1.set_xlim([s1[0]-0.5,s1[len(s1)-1]+0.5])
ax1.set_ylim([min(min(betax),min(betay))-5.,max(max(betax),max(betay))*1.05])
ax1.set_xlabel(r'$s\ (m)$',fontsize='xx-large')
ax1.set_ylabel(r'$\beta_{x,y}\ ({m})$',fontsize='x-large')
ax10 = fig1.add_axes([0.15, 0.875, 0.65, 0.05])
ax10.plot(s2,prof,c='k',lw=0.4) 
ax10.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
ax10.set_xticks([])
ax10.set_yticks([])
ax10.spines['right'].set_color('none')
ax10.spines['top'].set_color('none')
ax10.spines['bottom'].set_color('none')
ax10.spines['left'].set_color('none')
ax11= ax1.twinx()
l4 = ax11.plot(s1,etax,'r-.',ms=0.4)
l5 = ax11.plot(s1,etay,'y-.',ms=0.4)
plt1.eSetPlot(ax11)
ax11.set_xlim([ax10.get_xlim()[0],ax10.get_xlim()[1]])
ax11.set_ylim([min(min(etax),min(etay))-0.02,max(max(etax),max(etay))+0.02])
ax11.set_ylabel(r'$\eta_{x,y}\ (m)$',fontsize='x-large')
ax12=ax1.twinx()
ax12.yaxis.set_ticks_position('right')
ax12.spines['right'].set_position(('data', max(s1)*1.175))
ax12.set_ylim([-18,2])
l3 = ax12.plot(s1,cyy*1000,'k--')
plt1.eSetPlot(ax12)
ax12.set_ylabel(r'$\Delta_{y}\ (mm)$',fontsize='x-large')
plt.legend(l1+l2+l4+l5+l3,[r'$\beta_{x}$',r'$\beta_{y}$',r'$\eta_x$',r'$\eta_y$',r'$Y+C_y$'],frameon=False,loc="upper center",bbox_to_anchor=(0.50,1.015),ncol=3)

plt.show()
# fig1.savefig('../fig/kick/kick.png')


