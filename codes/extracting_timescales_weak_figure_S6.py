##this code generates subfigure S6b

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

x1,y1 = np.loadtxt('height_slow_eta_0.225_kf_4_19_cu_gel_0.6_step1_refined_mesh.csv',delimiter=',',unpack=True) #height profile generated from deform.pvd which is the output of weak_acid_1D_step_1.py using Paraview 5.7.0 

x4,y4 = np.loadtxt('height_slow_eta_0.225_kf_4_19_cu_gel_0.6_step2_refined_mesh.csv',delimiter=',',unpack=True)#height profile generated from deform.pvd which is the output of weak_acid_1D_step_2.py using Paraview 5.7.0 

x4 = x4 +8.4
#x3,y3 = np.loadtxt('experimental_data.csv',delimiter=',',unpack=True)
x2,y2 = np.loadtxt('fast_height_avg_2d.txt', unpack=True, comments='%')

#y3 = np.radians(y3)
#y3 = np.cos(y3)
#y3 = y3/np.cos(np.radians(9))


fig,ax = plt.subplots(1,1,figsize=(6.4,4.8))
fig.subplots_adjust(left=0.16)

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=32)#labelcolor = "white"

#tick labels
#ax.xaxis.set_ticks(np.arange(0.,28.1,7))
ax.yaxis.set_ticks(np.arange(-11,-0.9,5))

y1log = np.log(y1-y1[0])
y4log = np.log(y4-y1[0])
#plotting 1d gel height
ax.plot(x1,y1log, color='black', linewidth='5')
ax.plot(x4,y4log, color='black', linewidth='5')
#ax.set_xlim(0,128.4)
ax.set_ylim(-14,0)

#extracting timescales
m1= np.polyfit(x1[250:840],y1log[250:840],1)
x = np.concatenate((x1,x4))
y1fit = m1[0]*x + m1[1]
ax.plot(x[250:1700], y1fit[250:1700], color='black',linewidth=3)
ax.annotate(f'{-1/m1[0]:.2f}'+r'$\tau$',xy=(1.5,-9), color='black', fontsize='20')
m2= np.polyfit(x4[560:1560],y4log[560:1560],1)
y2fit = m2[0]*x4 + m2[1]
ax.plot(x4[560:3000], y2fit[560:3000],color='black',linewidth=3)
ax.annotate(f'{-1/m2[0]:.2f}'+r'$\tau$',xy=(32,-6.3), color='black', fontsize='20')
m3= np.polyfit(x4[2160:2660],y4log[2160:2660],1)
y3fit = m3[0]*x4 + m3[1]
ax.plot(x4[2160:3260], y3fit[2160:3260],color='black',linewidth=3)
ax.annotate(f'{-1/m3[0]:.2f}'+r'$\tau$',xy=(34,-12.5), color='black', fontsize='20')
m4= np.polyfit(x4[5160:],y4log[5160:],1)
y4fit = m4[0]*x4 + m4[1]
ax.plot(x4[4160:], y4fit[4160:],color='black',linewidth=3)
ax.annotate(f'{-1/m4[0]:.2f}'+r'$\tau$',xy=(90,-13), color='black',fontsize='20')
m5= np.polyfit(x1[5:20],y1log[5:20],1)
y5fit = m5[0]*x1 + m5[1]
#ax.plot(x1[0:40], y5fit[0:40],linewidth=2.5,color='0.85')
#ax.annotate(f'{1/m5[0]:.2f}'+r'$\tau$',xy=(-4.5,-2.6), color='0.85', fontsize='20')
m6= np.polyfit(x4[10:36],y4log[10:36],1)
y6fit = m6[0]*x4 + m6[1]
#ax.plot(x4[10:100], y6fit[10:100], linewidth=2.5,color='0.6')
#ax.annotate(f'{1/m6[0]:.2f}'+r'$\tau$',xy=(9.3,-4), color='0.6', fontsize='20')
#plt.ylabel(r'$ln(h_r/H)$', fontsize='25')
#plt.xlabel(r'$t/\tau$', fontsize='25')
plt.savefig('timescales_slow.png', bbox_inches='tight', pad_inches=0.0, dpi=300)
plt.show()


