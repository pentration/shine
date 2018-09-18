#!/usr/bin/env /usr/local/opt/anaconda/bin/python

import numpy as np
import scipy as sp
import math
import scipy.constants as spc
import string
import matplotlib.pyplot as plt
import enhancePlot as ep

plt.style.use('messiah')

s1,betax,cyy,betay = np.loadtxt('../dat/kick/kick.dat',usecols=(0,2,5,6),unpack=True,skiprows=2)
s2,prof = np.loadtxt('../dat/kick/prof.dat',unpack=True,skiprows=1)

fig1   = plt.figure()
ax1 = fig1.add_axes([0.15, 0.20, 0.70, 0.60])
plt1 = ep.enhancePlot(title=r'Optics of the Kicker Section, $l_{kicker}$=0.5m')
l1 = ax1.plot(s1,betax)
l2 = ax1.plot(s1,betay)
plt1.eSetPlot(ax1)
ax1.ticklabel_format(style='plain',axis='y')
ax1.set_xlim([0,25])
ax1.set_ylim([10,35])
ax1.set_xlabel(r'$s\ (m)$',fontsize='xx-large')
ax1.set_ylabel(r'$\beta_{x,y}\ ({m})$',fontsize='xx-large')
ax10 = fig1.add_axes([0.15, 0.875, 0.70, 0.05])
ax10.plot(s2,prof,c='k',lw=0.4) 
ax10.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
ax10.set_xticks([])
ax10.set_yticks([])
ax10.spines['right'].set_color('none')
ax10.spines['top'].set_color('none')
ax10.spines['bottom'].set_color('none')
ax10.spines['left'].set_color('none')
ax11= ax1.twinx()
l3 = ax11.plot(s1,cyy*1000,'k--')
plt1.eSetPlot(ax11,pltLabel=[r'$\Delta_y$'])
ax11.set_xlim([ax10.get_xlim()[0],ax10.get_xlim()[1]])
ax11.set_ylim([-5,20])
ax11.set_ylabel(r'$\Delta_y\ (mm)$',fontsize='xx-large')
plt.legend(l1+l2+l3,[r'$\beta_{x}$',r'$\beta_{y}$',r'$\Delta_{y}$'],frameon=False,loc="upper center",bbox_to_anchor=(0.50,1.015),ncol=3)

plt.show()
fig1.savefig('../fig/kick/beta.eps')


