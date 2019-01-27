#!/usr/bin/env /usr/local/opt/anaconda/bin/python

import numpy as np
import math
import scipy.constants as spc
import string
import matplotlib.pyplot as plt
plt.style.use('messiah')

s1,betax,betay,etax,etay,enx,eny,sigx,sigy,r56 = np.loadtxt('../../dat/ltu1/param.dat',usecols=(0,2,3,4,5,8,9,10,11,12),unpack=True,skiprows=2)
s2,prof = np.loadtxt('../../dat/ltu1/prof.dat',unpack=True,skiprows=1)

s1 = [s-88 for s in s1]
s2 = [s-88 for s in s2]

fig1   = plt.figure()
ax1 = fig1.add_axes([0.110, 0.140, 0.750, 0.710])
l1 = ax1.plot(s1,betax)
l2 = ax1.plot(s1,betay)
ax1.set_title(r'$\beta$-functions and dispersions of LTU-1',fontstyle='italic')
ax1.set_xlim([s1[0]-5,s1[-1]+5])
ax1.set_ylim([min(min(betax),min(betay))/2,max(max(betax),max(betay))*1.05])
ax1.set_xlabel(r'$s\ (m)$')
ax1.set_ylabel(r'$\beta_{x,y}\ ({m})$')
ax1.ticklabel_format(style='plain',axis='x')
ax10 = fig1.add_axes([0.110, 0.930, 0.750, 0.030])
ax10.plot(s2,prof,c='k',lw=0.4) 
ax10.set_xlim(ax1.get_xlim())
ax10.set_xticks([])
ax10.set_yticks([])
ax10.spines['right'].set_color('none')
ax10.spines['top'].set_color('none')
ax10.spines['bottom'].set_color('none')
ax10.spines['left'].set_color('none')
ax11= ax1.twinx()
l3 = ax11.plot(s1,etax,'--',c='y')
ax11.set_xlim(ax1.get_xlim())
ax11.set_ylim([min(etax)*1.05,max(etax)*1.05])
ax11.set_ylabel(r'$\eta_{x}\ (m)$')
plt.yticks(fontsize=14)
plt.legend(l1+l2+l3,[r'$\beta_{x}$',r'$\beta_{y}$',r'$\eta_{x}$'],loc=1,ncol=1)
# ax1.set_xticks([-120, -80, -40, 0, 44, 88, 120])
# ax1.set_xticklabels( ('-120', '-80', '-40', '0', '44', '88',  '120'))
#

fig4   = plt.figure()
ax4 = fig4.add_axes([0.110, 0.140, 0.750, 0.710])
l1 = ax4.plot(s1,enx*spc.mega)
l2 = ax4.plot(s1,eny*spc.mega)
ax4.set_title(r'Norm. Emittance of LTU-1',fontstyle='italic',fontweight='bold')
ax4.set_xlim(ax1.get_xlim())
ax4.set_ylim([min(min(enx),min(eny))*spc.mega/1.2,max(max(enx),max(eny))*spc.mega*1.02])
ax4.set_xlabel(r'$s\ (m)$')
ax4.set_ylabel(r'$\varepsilon_{x,y}\ (\mu{m}{\cdot}rad)$')
ax4.ticklabel_format(style='plain',axis='x')
plt.legend(l1+l2,[r'$\varepsilon_{x}$',r'$\varepsilon_{y}$'],loc=0,ncol=1)
ax40= fig4.add_axes([0.110, 0.930, 0.750, 0.030])
ax40.plot(s2,prof,c='k',lw=0.4)
ax40.set_xlim(ax1.get_xlim())
ax40.set_xticks([])
ax40.set_yticks([])
ax40.spines['right'].set_color('none')
ax40.spines['top'].set_color('none')
ax40.spines['bottom'].set_color('none')
ax40.spines['left'].set_color('none')


fig5   = plt.figure();
ax5 = fig5.add_axes([0.110, 0.140, 0.750, 0.710])
ax5.plot(s1,r56*spc.kilo)
ax5.set_xlim(ax1.get_xlim())
# # ax5.set_ylim([-0.2,0.2])
ax5.set_title(r'$R_{56}$')
ax5.set_xlabel(r'$s\ (m)$')
ax5.set_ylabel(r'$R_{56}\ (mm)$')
ax5.ticklabel_format(style='plain',axis='x')
ax50= fig5.add_axes([0.110, 0.930, 0.750, 0.030])
ax50.plot(s2,prof,c='k',lw=0.4)
ax50.set_xlim(ax1.get_xlim())
ax50.set_xticks([])
ax50.set_yticks([])
ax50.spines['right'].set_color('none')
ax50.spines['top'].set_color('none')
ax50.spines['bottom'].set_color('none')
ax50.spines['left'].set_color('none')

fig6   = plt.figure();
ax6 = fig6.add_axes([0.110, 0.140, 0.750, 0.710])
l1 = ax6.plot(s1,16*sigx*spc.kilo,label=r'$\sigma_x$')
l2 = ax6.plot(s1,16*sigy*spc.kilo,label=r'$\sigma_y$')
ax6.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
ax6.set_title(r'Beam Profile with Dispersion',fontstyle='italic')
ax6.set_xlabel(r'$s\ (m)$')
ax6.set_ylabel(r'$16*\sigma_{x,y}\ (mm)$')
ax6.ticklabel_format(style='plain',axis='x')
ax6.legend(loc=0)
ax60= fig6.add_axes([0.110, 0.930, 0.750, 0.030])
ax60.plot(s2,prof,c='k',lw=0.4)
ax60.set_xlim([ax6.get_xlim()[0],ax6.get_xlim()[1]])
ax60.set_xticks([])
ax60.set_yticks([])
ax60.spines['right'].set_color('none')
ax60.spines['top'].set_color('none')
ax60.spines['bottom'].set_color('none')
ax60.spines['left'].set_color('none')

# print(enx[0]*spc.mega,enx[len(enx)-1]*spc.mega,(enx[len(enx)-1]-enx[0])/enx[0])
# print(eny[0]*spc.mega,eny[len(eny)-1]*spc.mega,(eny[len(eny)-1]-eny[0])/eny[0])

plt.show()
# fig1.savefig('../../fig/ltu1/beta.eps')
# fig2.savefig('../../fig/ltu1/eta.eps')
# fig3.savefig('../../fig/ltu1/etap.eps')
# fig2.savefig('../../fig/ltu1/emitn.eps')
# fig3.savefig('../../fig/ltu1/r56.eps')
# fig6.savefig('../../fig/ltu1/sigma.eps')
#



