#!/usr/bin/env /usr/local/opt/anaconda/bin/python

import numpy as np
import math
import scipy.constants as spc
import string
import matplotlib.pyplot as plt
import enhancePlot as ep
plt.style.use('messiah')

s1,betax,betay,etax,etay,enx,eny,sigx,sigy,r56 = np.loadtxt('../../dat/ltu3/param.dat',usecols=(0,2,3,4,5,8,9,10,11,12),unpack=True,skiprows=2)
s2,prof = np.loadtxt('../../dat/ltu3/prof.dat',unpack=True,skiprows=1)

s1 = [s-88 for s in s1]
s2 = [s-88 for s in s2]

fig1   = plt.figure()
ax1 = fig1.add_axes([0.15, 0.20, 0.70, 0.60])
plt1 = ep.enhancePlot(title=r'$\beta$-functions and $x$-dispersion of LTU-3')
l1 = ax1.plot(s1,betax)
l2 = ax1.plot(s1,betay)
plt1.eSetPlot(ax1)
ax1.set_xlim([min(s1)-5,max(s1)+5])
ax1.set_ylim([min(min(betax),min(betay))/2,max(max(betax),max(betay))*1.05])
ax1.set_xlabel(r'$s\ (m)$',fontsize='xx-large')
ax1.set_ylabel(r'$\beta_{x,y}\ ({m})$',fontsize='xx-large')
ax1.ticklabel_format(style='plain',axis='y')
ax11 = fig1.add_axes([0.15, 0.875, 0.70, 0.05])
ax11.plot(s2,prof,c='k',lw=0.4) 
ax11.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
ax11.set_xticks([])
ax11.set_yticks([])
ax11.spines['right'].set_color('none')
ax11.spines['top'].set_color('none')
ax11.spines['bottom'].set_color('none')
ax11.spines['left'].set_color('none')
ax12= ax1.twinx()
l3 = plt1.ePlot(ax12,s1,etax,mt=['--'],cl=['y'])
plt1.eSetPlot(ax12)
ax12.set_xlim([ax11.get_xlim()[0],ax11.get_xlim()[1]])
ax12.set_ylim([min(etax)*1.05,max(etax)*1.05])
# ax12.set_ylim([-0.25,0.25])
ax12.set_ylabel(r'$\eta_{x}\ (m)$',fontsize=22)
plt.yticks(fontsize=14)
plt.legend(l1+l2+l3,[r'$\beta_{x}$',r'$\beta_{y}$',r'$\eta_{x}$'],fontsize=14,bbox_to_anchor=(0.50,1.025),ncol=3)
# ax1.set_xticks([-120, -80, -40, 0, 44, 88, 120])
# ax1.set_xticklabels( ('-120', '-80', '-40', '0', '44', '88',  '120'))
#

fig4   = plt.figure()
ax4 = fig4.add_axes([0.15, 0.20, 0.75, 0.60])
plt4 = ep.enhancePlot(axis=[r'$s\ (m)$',r'$\varepsilon_{x,y}\ (\mu{m}{\cdot}rad)$'],title='Norm. Emittance of LTU-3')
l1 = ax4.plot(s1,enx*spc.mega)
l2 = ax4.plot(s1,eny*spc.mega)
plt4.eSetPlot(ax4)
ax4.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
ax4.set_ylim([min(min(enx),min(eny))*spc.mega/1.2,max(max(enx),max(eny))*spc.mega*1.02])
plt.legend(l1+l2,[r'$\varepsilon_{x}$',r'$\varepsilon_{y}$'],fontsize=14,bbox_to_anchor=(0.50,1.025),ncol=3)
ax42= fig4.add_axes([0.15, 0.875, 0.75, 0.05])
ax42.plot(s2,prof,c='k',lw=0.4)
ax42.set_xlim([ax4.get_xlim()[0],ax4.get_xlim()[1]])
ax42.set_xticks([])
ax42.set_yticks([])
ax42.spines['right'].set_color('none')
ax42.spines['top'].set_color('none')
ax42.spines['bottom'].set_color('none')
ax42.spines['left'].set_color('none')


# # fig5   = plt.figure(figsize=(8,4), dpi=200, facecolor="white");
# fig5   = plt.figure();
# ax5 = fig5.add_axes([0.15, 0.20, 0.75, 0.60])
# plt5 = ep.enhancePlot(axis=[r'$s\ (m)$',r'$R_{56}\ (mm)$'],title=r'$R_{56}$')
# ax5.plot(s1,r56*spc.kilo)
# plt5.eSetPlot(ax5,legendFS=14)
# ax5.set_xlim([ax1.get_xlim()[0],ax1.get_xlim()[1]])
# # ax5.set_ylim([-0.2,0.2])
# ax52= fig5.add_axes([0.15, 0.875, 0.75, 0.05])
# ax52.plot(s2,prof,c='k',lw=0.4)
# ax52.set_xlim([ax5.get_xlim()[0],ax5.get_xlim()[1]])
# ax52.set_xticks([])
# ax52.set_yticks([])
# ax52.spines['right'].set_color('none')
# ax52.spines['top'].set_color('none')
# ax52.spines['bottom'].set_color('none')
# ax52.spines['left'].set_color('none')
# ax5.ticklabel_format(style='plain',axis='x')

# fig6   = plt.figure(figsize=(8,4), dpi=100, facecolor="white");
# ax6 = fig6.add_axes([0.15, 0.20, 0.70, 0.60])
# plt6 = ep.enhancePlot()
# plt6.ePlot(ax6,s1,sigx,sigy,pltLabel=[r'$\sigma_x$',r'$\sigma_y$'],axis=[r'$s\ (m)$',r'$\sigma_{x,y}\ (m)$'],title='Beam Profile with Dispersion')
# ax62= fig6.add_axes([0.15, 0.875, 0.70, 0.05])
# ax62.plot(s2,prof,c='k',lw=0.1)
# # ax62.set_ylim([-20,20])
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

print(enx[0]*spc.mega,enx[len(enx)-1]*spc.mega,(enx[len(enx)-1]-enx[0])/enx[0])
print(eny[0]*spc.mega,eny[len(eny)-1]*spc.mega,(eny[len(eny)-1]-eny[0])/eny[0])

plt.show()
fig1.savefig('../../fig/ltu3/beta.eps')
# fig2.savefig('../../fig/ltu3/eta.eps')
# fig3.savefig('../../fig/ltu3/etap.eps')
# fig2.savefig('../../fig/ltu3/emitn.eps')
# fig3.savefig('../../fig/ltu3/r56.eps')
# fig6.savefig('../../fig/ltu3/sigma.eps')
#



