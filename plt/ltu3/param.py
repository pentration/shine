#!/usr/bin/env /usr/local/opt/anaconda/bin/python

import numpy as np
import scipy as sp
import math
import scipy.constants as spc
# import scipy.special as sps
import string
import matplotlib.pyplot as plt
import enhancePlot as ep
# import os
# import re
plt.style.use('messiah')
# plt.style.use('classic')

# os.system('./run/runScript')
s1,betax,betay,etax,etay,enx,eny,sigx,sigy,r56 = np.loadtxt('../../dat/ltu3/param.dat',usecols=(0,2,3,4,5,8,9,10,11,12),unpack=True,skiprows=3)
s2,prof = np.loadtxt('../../dat/ltu3/prof.dat',unpack=True,skiprows=1)

fig1   = plt.figure()
ax1 = fig1.add_axes([0.15, 0.20, 0.70, 0.60])
plt1 = ep.enhancePlot(title=r'$\beta$-functions and $x$-dispersion')
l1 = ax1.plot(s1-208,betax)
l2 = ax1.plot(s1-208,betay)
plt1.eSetPlot(ax1)
ax1.ticklabel_format(style='plain',axis='y')
ax1.set_xlim([-240,400])
ax1.set_ylim([-10,250])
ax1.set_xlabel(r'$s\ (m)$',fontsize='xx-large')
ax1.set_ylabel(r'$\beta_{x,y}\ ({m})$',fontsize='xx-large')
ax10 = fig1.add_axes([0.15, 0.875, 0.70, 0.05])
ax10.plot(s2-208,prof,c='k',lw=0.4) 
ax10.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
ax10.set_xticks([])
ax10.set_yticks([])
ax10.spines['right'].set_color('none')
ax10.spines['top'].set_color('none')
ax10.spines['bottom'].set_color('none')
ax10.spines['left'].set_color('none')
ax11= ax1.twinx()
l3 = ax11.plot(s1-208,etax,'--',c='y')
plt1.eSetPlot(ax11,pltLabel=[r'$\eta_x$'])
ax11.set_xlim([ax10.get_xlim()[0],ax10.get_xlim()[1]])
ax11.set_ylim([-0.25,0.25])
# ax11.ticklabel_format(style='plain',axis='y')
ax11.set_ylabel(r'$\eta_{x}\ (m)$',fontsize='xx-large')
ax11.set_xticks([       -208 ,  -88 ,  0 ,  50 ,   100 ,   150 ,   200 ,  250 ,  300 ,  370 ])
ax11.set_xticklabels( ('-208', '-88', '0', '50',  '100',  '150',  '200', '250', '300', '370'))
ax11.set_yticks([-0.2, -0.1, 0.0, 0.1, 0.2 ])
ax11.set_yticklabels(('-0.2', '-0.1', '0.0', '0.1', '0.2'))
ax1.text(-164,ax1.get_ylim()[1]-0.18*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    'Linac',fontsize=10,ha='center',va='center')
ax1.text(-164,ax1.get_ylim()[1]-0.24*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    'Tunnel',fontsize=10,ha='center',va='center')
ax1.text(-44,ax1.get_ylim()[1]-0.18*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    '#2',fontsize=10,ha='center',va='center')
ax1.text(-44,ax1.get_ylim()[1]-0.24*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    'Shaft',fontsize=10,ha='center',va='center')
ax1.text(200,ax1.get_ylim()[1]-0.18*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    'West',fontsize=10,ha='center',va='center')
ax1.text(200,ax1.get_ylim()[1]-0.24*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    'Und-Tunnel',fontsize=10,ha='center',va='center')
ax1.text(200,ax1.get_ylim()[0]+0.08*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    'FEL-III Undulator Line',fontsize=10,ha='center',va='center')
ax1.text(370,ax1.get_ylim()[0]+0.53*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    'Light',fontsize=10,ha='center',va='center')
ax1.text(370,ax1.get_ylim()[0]+0.47*(ax1.get_ylim()[1]-ax1.get_ylim()[0]),
    'Point',fontsize=10,ha='center',va='center')
plt.legend(l1+l2+l3,[r'$\beta_{x}$',r'$\beta_{y}$',r'$\eta_{x}$'],
    frameon=False,loc="upper center",bbox_to_anchor=(0.50,1.025),ncol=3)
line1=[(-88,-20),(-88,280)]
line2=[(0,-20),(0,280)]
line3=[(370,-20),(370,280)]
(line1_xs,line1_ys)=zip(*line1)
(line2_xs,line2_ys)=zip(*line2)
(line3_xs,line3_ys)=zip(*line3)
ax1.add_line(plt.Line2D(line1_xs,line1_ys,linestyle=':',linewidth=0.5,color='k'))
ax1.add_line(plt.Line2D(line2_xs,line2_ys,linestyle=':',linewidth=0.5,color='k'))
ax1.add_line(plt.Line2D(line3_xs,line3_ys,linestyle=':',linewidth=0.5,color='k'))

# fig2   = plt.figure();
# ax2 = fig2.add_axes([0.15, 0.20, 0.70, 0.60])
# plt2 = ep.enhancePlot()
# l1 = plt2.ePlot(ax2,s1,enx,eny)
# # ax20= ax2.twinx()
# plt2.eSetPlot(ax2,axis=[r'$s\ (m)$',r'$\varepsilon_{x,y}\ (\mu{m}{\cdot}rad)$'],legendOn=False)
# ax2.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
# ax2.set_ylim([0.2,1.0])
# plt.legend(l1,[r'$\varepsilon_{x}$',r'$\varepsilon_{y}$'],bbox_to_anchor=(0.50,1.12),ncol=2)
# ax20= fig2.add_axes([0.15, 0.875, 0.70, 0.05])
# ax20.plot(s2,prof,c='k',lw=0.4)
# ax20.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
# ax20.set_xticks([])
# ax20.set_yticks([])
# ax20.spines['right'].set_color('none')
# ax20.spines['top'].set_color('none')
# ax20.spines['bottom'].set_color('none')
# ax20.spines['left'].set_color('none')
# ax2.ticklabel_format(style='plain',axis='x')
# ax2.set_xticks([-132.5, -88, 0, 50,  100,  150,  200, 250, 300])
# ax2.set_xticklabels( ('-132.5', '-88', '0', '50',  '100',  '150',  '200', '250', '300'))
# ax2.text(-120,ax2.get_ylim()[1]-0.18*(ax2.get_ylim()[1]-ax2.get_ylim()[0]),'Linac',fontsize=10,ha='center',va='center')
# ax2.text(-120,ax2.get_ylim()[1]-0.24*(ax2.get_ylim()[1]-ax2.get_ylim()[0]),'Tunnel',fontsize=10,ha='center',va='center')
# ax2.text(-44,ax2.get_ylim()[1]-0.18*(ax2.get_ylim()[1]-ax2.get_ylim()[0]),'#2',fontsize=10,ha='center',va='center')
# ax2.text(-44,ax2.get_ylim()[1]-0.24*(ax2.get_ylim()[1]-ax2.get_ylim()[0]),'Shaft',fontsize=10,ha='center',va='center')
# ax2.text(175,ax2.get_ylim()[1]-0.18*(ax2.get_ylim()[1]-ax2.get_ylim()[0]),'FEL',fontsize=10,ha='center',va='center')
# ax2.text(175,ax2.get_ylim()[1]-0.24*(ax2.get_ylim()[1]-ax2.get_ylim()[0]),'Tunnel',fontsize=10,ha='center',va='center')
# ax2.text(175,ax2.get_ylim()[0]+0.16*(ax2.get_ylim()[1]-ax2.get_ylim()[0]),'FEL-2 Undulator Line',fontsize=10,ha='center',va='center')
# ax20.set_xlim([ax2.get_xlim()[0],ax2.get_xlim()[1]])
# ax2.add_line(plt.Line2D(line1_xs,line1_ys,linestyle=':',linewidth=2,color='k'))
# ax2.add_line(plt.Line2D(line2_xs,line2_ys,linestyle=':',linewidth=2,color='k'))
#
# fig3   = plt.figure();
# ax3 = fig3.add_axes([0.15, 0.20, 0.70, 0.60])
# plt3 = ep.enhancePlot()
# l1 = plt3.ePlot(ax3,s1,r56)
# plt3.eSetPlot(ax3,axis=[r'$s\ (m)$',r'$R_{56}\ (mm)$'])
# ax3.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
# ax30= fig3.add_axes([0.15, 0.875, 0.70, 0.05])
# ax30.plot(s2,prof,c='k',lw=0.4)
# ax30.set_xticks([])
# ax30.set_yticks([])
# ax30.spines['right'].set_color('none')
# ax30.spines['top'].set_color('none')
# ax30.spines['bottom'].set_color('none')
# ax30.spines['left'].set_color('none')
# ax3.ticklabel_format(style='plain',axis='x')
# ax3.set_xticks([-132.5, -88, 0, 50,  100,  150,  200, 250, 300])
# ax3.set_xticklabels( ('-132.5', '-88', '0', '50',  '100',  '150',  '200', '250', '300'))
# ax3.text(-120,ax3.get_ylim()[1]-0.18*(ax3.get_ylim()[1]-ax3.get_ylim()[0]),'Linac',fontsize=10,ha='center',va='center')
# ax3.text(-120,ax3.get_ylim()[1]-0.24*(ax3.get_ylim()[1]-ax3.get_ylim()[0]),'Tunnel',fontsize=10,ha='center',va='center')
# ax3.text(-44,ax3.get_ylim()[1]-0.18*(ax3.get_ylim()[1]-ax3.get_ylim()[0]),'#2',fontsize=10,ha='center',va='center')
# ax3.text(-44,ax3.get_ylim()[1]-0.24*(ax3.get_ylim()[1]-ax3.get_ylim()[0]),'Shaft',fontsize=10,ha='center',va='center')
# ax3.text(175,ax3.get_ylim()[1]-0.18*(ax3.get_ylim()[1]-ax3.get_ylim()[0]),'FEL',fontsize=10,ha='center',va='center')
# ax3.text(175,ax3.get_ylim()[1]-0.24*(ax3.get_ylim()[1]-ax3.get_ylim()[0]),'Tunnel',fontsize=10,ha='center',va='center')
# ax3.text(175,ax3.get_ylim()[0]+0.16*(ax3.get_ylim()[1]-ax3.get_ylim()[0]),'FEL-2 Undulator Line',fontsize=10,ha='center',va='center')
# ax30.set_xlim([ax3.get_xlim()[0],ax3.get_xlim()[1]])
# ax3.add_line(plt.Line2D(line1_xs,line1_ys,linestyle=':',linewidth=2,color='k'))
# ax3.add_line(plt.Line2D(line2_xs,line2_ys,linestyle=':',linewidth=2,color='k'))


# fig6   = plt.figure();
# ax6 = fig6.add_axes([0.15, 0.20, 0.75, 0.60])
# plt6 = ep.enhancePlot()
# l1  = ax6.plot(s1-208,sigx*10)
# l2  = ax6.plot(s1-208,sigy*10)
# plt6.eSetPlot(ax6,axis=[r'$s\ (m)$',r'$10*\sigma_{x,y}\ (m)$'],title='Beam Profile with Dispersion')
# plt.legend(l1+l2,[r'$10*\sigma_{x}$',r'$10*\sigma_{y}$'],frameon=False,loc="upper center",bbox_to_anchor=(0.50,1.025),ncol=2)
# ax6.set_xlim([-240,400])
# ax62= fig6.add_axes([0.15, 0.875, 0.75, 0.05])
# ax62.plot(s2-208,prof,c='k',lw=0.4)
# ax62.set_xlim([ax6.get_xlim()[0],ax6.get_xlim()[1]])
# ax62.set_xticks([])
# ax62.set_yticks([])
# ax62.spines['right'].set_color('none')
# ax62.spines['top'].set_color('none')
# ax62.spines['bottom'].set_color('none')
# ax62.spines['left'].set_color('none')
# plt6.eSetPlot(ax6,legendFS=14)
# ax6.ticklabel_format(style='plain',axis='x')
# ax6.set_xticks([-132.5, -88, 0, 50,  100,  150,  200, 250, 300, 350])
# ax6.set_xticklabels( ('-132.5', '-88', '0', '50',  '100',  '150',  '200', '250', '300', '350'))

plt.show()
fig1.savefig('../../fig/ltu3/beta.eps')
# fig2.savefig('../../fig/ltu3/eta.eps')
# fig3.savefig('../../fig/ltu3/etap.eps')
# fig2.savefig('../../fig/ltu3/emitn.eps')
# fig3.savefig('../../fig/ltu3/r56.eps')
# fig6.savefig('../../fig/ltu3/sigma.eps')
#


