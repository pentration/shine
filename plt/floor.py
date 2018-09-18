#!/usr/bin/env /usr/local/opt/anaconda/bin/python

import numpy as np
import scipy as sp
import scipy.constants as spc
# import scipy.special as sps
import string
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import enhancePlot as ep
# import os
# import re
plt.style.use('messiah')
# plt.style.use('classic')

# os.system('./run/runScript')

file1 = open("../dat/flr/ltu1-flr.dat")
file2 = open("../dat/flr/ltu2-flr.dat")
file3 = open("../dat/flr/ltu3-flr.dat")
file4 = open("../dat/flr/ltu4-flr.dat")
file5 = open("../dat/flr/ltu5-flr.dat")

data1 = [line.rstrip("\n") for line in file1]
data2 = [line.rstrip("\n") for line in file2]
data3 = [line.rstrip("\n") for line in file3]
data4 = [line.rstrip("\n") for line in file4]
data5 = [line.rstrip("\n") for line in file5]


ltu1 = np.transpose(([x.split()[1:] for x in data1[1:]]))
ltu2 = np.transpose(([x.split()[1:] for x in data2[1:]]))
ltu3 = np.transpose(([x.split()[1:] for x in data3[1:]]))
ltu4 = np.transpose(([x.split()[1:] for x in data4[1:]]))
ltu5 = np.transpose(([x.split()[1:] for x in data5[1:]]))

Z1 = [float(s)-63 for s in ltu1[3]]
Z2 = [float(s)-183 for s in ltu2[3]]
Z3 = [float(s)-133 for s in ltu3[3]]
Z4 = [float(s)-183 for s in ltu4[3]]
Z5 = [float(s)-183 for s in ltu5[3]]
X1 = [float(x)-0.2 for x in ltu1[1]]
X2 = [float(x)-0.2 for x in ltu2[1]]
X3 = [float(x)-0.2 for x in ltu3[1]]
X4 = [float(x)-0.2 for x in ltu4[1]]
X5 = [float(x)-0.2 for x in ltu5[1]]

R=1500
theta=np.linspace(-2,0)*np.pi/180
rho=2*R*np.sin(theta)
z=R*np.sin(theta)-208
xt1=R*(1-np.cos(theta))+2.67
xt2=R*(1-np.cos(theta))-2.67


fig1   = plt.figure()
ax1 = fig1.add_axes([0.10, 0.15, 0.80, 0.80])
plt1 = ep.enhancePlot()
ltu1 = plt1.ePlot(ax1, Z1, X1)
ltu2 = plt1.ePlot(ax1, Z2, X2)
ltu3 = plt1.ePlot(ax1, Z3, X3)
# l5 = plt1.ePlot(ax1, Z5, X5)
ltu4 = plt1.ePlot(ax1, Z4, X4, mt=(':'),lw=0.5)
ltu5 = plt1.ePlot(ax1, Z5, X5, mt=(':'),lw=0.5)
ax1.plot(z,xt1,lw=2,c='k')
ax1.plot(z,xt2,lw=2,c='k')
plt1.eSetPlot(ax1)
ax1.ticklabel_format(style='plain',axis='y')
ax1.set_xlim([-208,200])
ax1.set_ylim([-20,20])
ax1.set_xlabel(r'$s\ (m)$',fontsize='xx-large')
ax1.set_ylabel(r'$X\ ({m})$',fontsize='xx-large')
line00=[(-208,-0.0),(0,-0.0)]
line01=[(-208,-0.2),(-20,-0.2)]
line02=[(00,-16),(00,16)]
line03=[(00,-2.95),(200,-2.95)]
line04=[(00, 2.95),(200, 2.95)]
line05=[(00,-2.95-4.7),(200,-2.95-4.7)]
line06=[(00, 2.95+4.7),(200, 2.95+4.7)]
line07=[(00,-2.95-4.7-5.9),(200,-2.95-4.7-5.9)]
line08=[(00, 2.95+4.7+5.9),(200, 2.95+4.7+5.9)]
line09=[(-208,-2.67),(-88,-2.67)]
line10=[(-208, 2.67),(-88, 2.67)]
line11=[( -88,-2.67),(-88,-16)]
line12=[( -88, 2.67),(-88, 16)]
line13=[( -88,-16),(00,-16)]
line14=[( -88, 16),(00, 16)]
line15=[( 00,-16+2.45),(00,-16)]
line16=[( 00, 16-2.45),(00, 16)]

# line1=[(-21.487,-20),(-21.487,1.65)]
line17=[(-208,-5.5),(-208,-0.2)]
line18=[(-183,-5.5),(-183,-0.2)]
line19=[(-208,6.5),(-208,-0.2)]
line20=[(146,12.25),(146,4.5)]
line21=[(-158,-5.5),(-158,-0.2)]
line22=[(28.7314,-10.5),(28.7314,-9.1)]
line23=[(-63,-4.5),(-63,-0.2)]
line24=[(9.345-10,-4.5),(9.345-10,-1.65)]
line25=[(-133,-5.5),(-133,-0.2)]
line26=[(-20,3.5),(-20,-0.2)]
line27=[( 00,10.6),(200,10.6)]
line28=[( 00,-10.6),(200,-10.6)]
line29=[( 00,0.0),(200,0.0)]
ax1.text(-208,-6.0,'Kicker',fontsize=8,ha='center',va='center')
ax1.text(-183,-6.0,'Septum',fontsize=8,ha='center',va='center')
ax1.text(-158,-6.0,'Kicker',fontsize=8,ha='center',va='center')
ax1.text(-133,-6.0,'Septum',fontsize=8,ha='center',va='center')
ax1.text(-20,4.0,'Dump',fontsize=8,ha='center',va='center')
ax1.text(-44,13,'#2 Shaft',fontsize=10,ha='center',va='center')
ax1.text(-160,-2.0,'Linac Tunnel',fontsize=10,ha='center',va='center')
ax1.text(50, 00.000,'Mid Undulator Tunnel', fontsize=10,ha='center',va='center')
ax1.text(50, 12.075,'East Undulator Tunnel',fontsize=10,ha='center',va='center')
ax1.text(50,-12.075,'West Undulator Tunnel',fontsize=10,ha='center',va='center')
# ax1.annotate('',xy=(-208,6),xytext=(121+25,6),arrowprops=dict(arrowstyle="<->",linewidth=0.5,connectionstyle="arc3"))
# ax1.text(-20,6.5,'LTU2',fontsize=8,ha='center',va='center')
# ax1.annotate('',xy=(-158,-10),xytext=(28.7314,-10),arrowprops=dict(arrowstyle="<->",linewidth=0.5,connectionstyle="arc3"))
# ax1.text(-44,-10.7,'LTU3',fontsize=8,ha='center',va='center')
# ax1.annotate('',xy=(-63,-4),xytext=(9.345-10,-4),arrowprops=dict(arrowstyle="<->",linewidth=0.5,connectionstyle="arc3"))
# ax1.text(-40,-4.7,'LTU1',fontsize=8,ha='center',va='center')
# ax1.text(-44, 5.00,'LTU4',fontsize=8,ha='center',va='center')
# ax1.text(150, 1.65,'FEL-II',fontsize=8,ha='center',va='center')
ax1.text(175,-1.65,'FEL-I',fontsize=8,ha='center',va='center')
ax1.text(175,-9.10,'FEL-III',fontsize=8,ha='center',va='center')
# ax1.text(175, 8.90,'FEL-IV',fontsize=8,ha='center',va='center')
ax1.text(175, 12.25,'FEL-II',fontsize=8,ha='center',va='center')
(line00_xs,line00_ys)=zip(*line00)
(line01_xs,line01_ys)=zip(*line01)
(line02_xs,line02_ys)=zip(*line02)
(line03_xs,line03_ys)=zip(*line03)
(line04_xs,line04_ys)=zip(*line04)
(line05_xs,line05_ys)=zip(*line05)
(line06_xs,line06_ys)=zip(*line06)
(line07_xs,line07_ys)=zip(*line07)
(line08_xs,line08_ys)=zip(*line08)
(line09_xs,line09_ys)=zip(*line09)
(line10_xs,line10_ys)=zip(*line10)
(line11_xs,line11_ys)=zip(*line11)
(line12_xs,line12_ys)=zip(*line12)
(line13_xs,line13_ys)=zip(*line13)
(line14_xs,line14_ys)=zip(*line14)
(line15_xs,line15_ys)=zip(*line15)
(line16_xs,line16_ys)=zip(*line16)
(line17_xs,line17_ys)=zip(*line17)
(line18_xs,line18_ys)=zip(*line18)
(line19_xs,line19_ys)=zip(*line19)
(line20_xs,line20_ys)=zip(*line20)
(line19_xs,line19_ys)=zip(*line19)
(line20_xs,line20_ys)=zip(*line20)
(line21_xs,line21_ys)=zip(*line21)
(line22_xs,line22_ys)=zip(*line22)
(line23_xs,line23_ys)=zip(*line23)
(line24_xs,line24_ys)=zip(*line24)
(line25_xs,line25_ys)=zip(*line25)
(line26_xs,line26_ys)=zip(*line26)
(line27_xs,line27_ys)=zip(*line27)
(line28_xs,line28_ys)=zip(*line28)
(line29_xs,line29_ys)=zip(*line29)
ax1.add_line(plt.Line2D(line00_xs,line00_ys,linestyle=':',linewidth=0.1,color='r'))
ax1.add_line(plt.Line2D(line01_xs,line01_ys,linestyle='-',linewidth=1.,color='b'))
ax1.add_line(plt.Line2D(line02_xs,line02_ys,linestyle=':',linewidth=.5,color='k'))
ax1.add_line(plt.Line2D(line03_xs,line03_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line04_xs,line04_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line05_xs,line05_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line06_xs,line06_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line07_xs,line07_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line08_xs,line08_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line09_xs,line09_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line10_xs,line10_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line11_xs,line11_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line12_xs,line12_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line13_xs,line13_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line14_xs,line14_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line15_xs,line15_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line16_xs,line16_ys,linestyle='-',linewidth=2,color='k'))
ax1.add_line(plt.Line2D(line17_xs,line17_ys,linestyle=':',linewidth=1,color='k'))
ax1.add_line(plt.Line2D(line18_xs,line18_ys,linestyle=':',linewidth=1,color='k'))
# ax1.add_line(plt.Line2D(line19_xs,line19_ys,linestyle=':',linewidth=1,color='k'))
# ax1.add_line(plt.Line2D(line20_xs,line20_ys,linestyle=':',linewidth=1,color='k'))
ax1.add_line(plt.Line2D(line21_xs,line21_ys,linestyle=':',linewidth=1,color='k'))
# ax1.add_line(plt.Line2D(line22_xs,line22_ys,linestyle=':',linewidth=1,color='k'))
# ax1.add_line(plt.Line2D(line23_xs,line23_ys,linestyle=':',linewidth=1,color='k'))
# ax1.add_line(plt.Line2D(line24_xs,line24_ys,linestyle=':',linewidth=1,color='k'))
ax1.add_line(plt.Line2D(line25_xs,line25_ys,linestyle=':',linewidth=1,color='k'))
ax1.add_line(plt.Line2D(line26_xs,line26_ys,linestyle=':',linewidth=1,color='k'))
ax1.add_line(plt.Line2D(line27_xs,line27_ys,linestyle=':',linewidth=0.25,color='k'))
ax1.add_line(plt.Line2D(line28_xs,line28_ys,linestyle=':',linewidth=0.25,color='k'))
ax1.add_line(plt.Line2D(line29_xs,line29_ys,linestyle=':',linewidth=0.25,color='k'))
# ax1.add_line(plt.Line2D(line25_xs,line25_ys,linestyle=':',linewidth=1,color='k'))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_color('none')
ax1.spines['left'].set_color('none')
ax1.set_xticks([-208,-158,-120,-88,-44,0,40,80,120,160,200])
ax1.set_yticks([])
plt.legend(ltu1+ltu2+ltu3,[r'LTU1',r'LTU2',r'LTU3'],frameon=False,loc="upper left",bbox_to_anchor=(0.00,0.925),fontsize=12)


# fig2   = plt.figure()
# ax2 = fig2.add_axes([0.10, 0.15, 0.80, 0.80])
# plt2 = ep.enhancePlot()
# ltu2 = plt2.ePlot(ax2, Z5, Y5)
# plt2.eSetPlot(ax2)
# ax2.ticklabel_format(style='plain',axis='y')
# ax2.set_xlim([-12,15])
# ax2.set_ylim([-6,1.0])
# ax2.set_xlabel(r'$s\ (m)$',fontsize='xx-large')
# ax2.set_ylabel(r'$Y\ ({m})$',fontsize='xx-large')
# line0=[(-12,-1.3),(15,-1.3)]
# line1=[(0,-6),(0,-1.72684)]
# line2=[(-12,-2.05),(15,-2.05)]
# line3=[(-10,-6),(-10,0)]
# line4=[(13.34643,-6),(13.34643,-5.3)]
# line5=[(-2.881122,-6),(-2.881122, -0.9245)]
# # line6=[(88,-2.95-4.7),(150,-2.95-4.7)]
# # line7=[(88, 2.95+4.7),(150, 2.95+4.7)]
# # line8=[(88,-2.95-4.7-5.9),(150,-2.95-4.7-5.9)]
# # line9=[(88, 2.95+4.7+5.9),(150, 2.95+4.7+5.9)]
# # line10=[(-208,-2.67),(00,-2.67)]
# # line11=[(-208, 2.67),(00, 2.67)]
# # line12=[( 00,-2.67),(00,-16)]
# # line13=[( 00, 2.67),(00, 16)]
# # line14=[( 00,-16),(88,-16)]
# # line15=[( 00, 16),(88, 16)]
# # line16=[( 88,-16+2.45),(88,-16)]
# # line17=[( 88, 16-2.45),(88, 16)]
# # line18=[(-45,-20),(-45,-0.2)]
# # line19=[(15,-20),(15,-0.2)]
# # line20=[(45,-20),(45,-0.2)]
# # line21=[(68,-20),(68,-0.2)]
# (line0_xs,line0_ys)=zip(*line0)
# (line1_xs,line1_ys)=zip(*line1)
# (line2_xs,line2_ys)=zip(*line2)
# (line3_xs,line3_ys)=zip(*line3)
# (line4_xs,line4_ys)=zip(*line4)
# (line5_xs,line5_ys)=zip(*line5)
# # (line6_xs,line6_ys)=zip(*line6)
# # (line7_xs,line7_ys)=zip(*line7)
# # (line8_xs,line8_ys)=zip(*line8)
# # (line9_xs,line9_ys)=zip(*line9)
# # (line10_xs,line10_ys)=zip(*line10)
# # (line11_xs,line11_ys)=zip(*line11)
# # (line12_xs,line12_ys)=zip(*line12)
# # (line13_xs,line13_ys)=zip(*line13)
# # (line14_xs,line14_ys)=zip(*line14)
# # (line15_xs,line15_ys)=zip(*line15)
# # (line16_xs,line16_ys)=zip(*line16)
# # (line17_xs,line17_ys)=zip(*line17)
# # (line18_xs,line18_ys)=zip(*line18)
# # (line19_xs,line19_ys)=zip(*line19)
# # (line20_xs,line20_ys)=zip(*line20)
# # (line21_xs,line21_ys)=zip(*line21)
# ax2.add_line(plt.Line2D(line0_xs,line0_ys,linestyle=':',linewidth=0.5,color='k'))
# ax2.add_line(plt.Line2D(line1_xs,line1_ys,linestyle=':',linewidth=0.5,color='k'))
# ax2.add_line(plt.Line2D(line2_xs,line2_ys,linestyle=':',linewidth=0.5,color='k'))
# ax2.add_line(plt.Line2D(line3_xs,line3_ys,linestyle=':',linewidth=0.5,color='k'))
# ax2.add_line(plt.Line2D(line4_xs,line4_ys,linestyle=':',linewidth=0.5,color='k'))
# ax2.add_line(plt.Line2D(line5_xs,line5_ys,linestyle=':',linewidth=0.5,color='k'))
# # ax2.add_line(plt.Line2D(line6_xs,line6_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line7_xs,line7_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line8_xs,line8_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line9_xs,line9_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line10_xs,line10_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line11_xs,line11_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line12_xs,line12_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line13_xs,line13_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line14_xs,line14_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line15_xs,line15_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line16_xs,line16_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line17_xs,line17_ys,linestyle='-',linewidth=2,color='k'))
# # ax2.add_line(plt.Line2D(line18_xs,line18_ys,linestyle=':',linewidth=1,color='k'))
# # ax2.add_line(plt.Line2D(line19_xs,line19_ys,linestyle=':',linewidth=1,color='k'))
# # ax2.add_line(plt.Line2D(line20_xs,line20_ys,linestyle=':',linewidth=1,color='k'))
# # ax2.add_line(plt.Line2D(line21_xs,line21_ys,linestyle=':',linewidth=1,color='k'))
# ax2.spines['right'].set_color('none')
# ax2.spines['top'].set_color('none')
# ax2.spines['bottom'].set_color('none')
# ax2.spines['left'].set_color('none')
# ax2.set_xticks([-10,-2.9,0,10,13.34643])
# ax2.set_yticks([-5.3,-2.01,-1.3,0,1])
# # ax2.set_yticks([])


plt.show()
fig1.savefig('../fig/flr/floor3.eps')
# fig2.savefig('../fig/flr/arc.eps')
# # fig2.savefig('../fig/eta.eps')
# # fig3.savefig('../fig/etap.eps')
# fig2.savefig('../fig/emitn.eps')
# fig3.savefig('../fig/r56.eps')
# # fig6.savefig('../fig/sigma.eps')
# #
file1.close()



