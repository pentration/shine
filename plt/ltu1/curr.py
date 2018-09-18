#!/usr/bin/env /usr/local/opt/anaconda/bin/python

# import scipy as sp
import numpy as np
import scipy.constants as spc
import string
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import enhancePlot as ep
#import os
# import re

plt.style.use('messiah')

file2 = open("../../dat/ltu1/current.dat")
file3 = open("../../dat/ltu1/current0.dat")

line2 = file2.readline()
line3 = file3.readline()

ct=[]
t=[]
lhoff=[]
lhon1=[]
lhon0=[]
# ipk1=[]
idx2=0

while line2:
    ipk1 = line2.split()
    ipk0 = line3.split()
    if idx2==0:
        sliceNum=string.atof(ipk1[0])
    else:
        ct.append(string.atof(ipk1[0])*spc.mega)
        t.append(string.atof(ipk1[1])*spc.tera)
        lhon1.append(string.atof(ipk1[2])/spc.kilo)
        lhon0.append(string.atof(ipk0[2])/spc.kilo)
    idx2 = idx2 + 1
    line2 = file2.readline()
    line3 = file3.readline()

fig6   = plt.figure();
ax6 = fig6.add_axes([0.15, 0.20, 0.70, 0.70])
plt.sca(ax6)
plt6 = ep.enhancePlot()
l1 = plt6.ePlot(ax6,ct,lhon1,lhon0)
plt6.eSetPlot(ax6,axis=[r'$ct\ ({\mu}m)$',r'$I_{pk}\ (kA)$'])
ax6.set_ylim([0,np.max([np.max(lhon1),np.max(lhon0)])*1.1])
ax6.legend(l1,[r'End of LTU1',r'End of Linac'],bbox_to_anchor=(0.50,1.10),ncol=2)
fig6.savefig('../../fig/ltu1/ipk.eps')

plt.show()
file2.close()
