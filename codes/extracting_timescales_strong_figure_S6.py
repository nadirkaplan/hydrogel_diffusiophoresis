##this code creates subfigure S6a

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

x1,y1 = np.loadtxt('height_fast_eta_0.225_kf_4_19_cu_gel_0.6_refined_mesh.csv',delimiter=',',unpack=True) #height profile generated from deform.pvd which is the output of strong_acid_1D.py using Paraview 5.7.0 
#x3,y3 = np.loadtxt('experimental_data.csv',delimiter=',',unpack=True)
#x2,y2 = np.loadtxt('fast_height_avg_2d.txt', unpack=True, comments='%')

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
ax.xaxis.set_ticks(np.arange(0.,12.1,4))
ax.yaxis.set_ticks(np.arange(-11,0,5))

y1log = np.log(y1-y1[0])
#plotting 1d gel height
ax.plot(x1,y1log, color='black', linewidth='5')
ax.set_xlim(-1,12.1)
ax.set_ylim(-14, 0)


#extracting timescales
m1= np.polyfit(x1[120:250],y1log[120:250],1)
y1fit = m1[0]*x1 + m1[1]
m2 = np.polyfit(x1[600:1200], y1log[600:1200],1)
y2fit = m2[0]*x1 + m2[1]
m3 = np.polyfit(x1[1:12], y1log[1:12],1)
y3fit = m3[0]*x1 + m3[1]
#theoretical estimate of relaxation ts
tau_d = 0.4
m4 = -1/0.4
y4fit = m4*x1 + -0.4

ax.plot(x1[120:600], y1fit[120:600], color='black', linewidth=3)
ax.plot(x1[400:1200], y2fit[400:1200], color='black', linewidth=3)
ax.plot(x1[120:300], y4fit[120:300], color='black', linewidth=3)
#ax.plot(x1[:18], y3fit[:18], color='0.85', linewidth=2.5)
ax.annotate(r'$\tau_{r,1}=$'+f'{-1/m1[0]:.2f}'+r'$\tau$',xy=(3.19,-12.69), fontsize='20', color='black')
ax.annotate(r'$\tau_{r,2}=$'+f'{-1/m2[0]:.2f}'+r'$\tau$',xy=(7.5,-7.5), fontsize='20', color='black')
ax.annotate(r'$\tau_{D}=$'+f'{tau_d:.1f}'+r'$\tau$',xy=(0.19,-9), fontsize='20', color='black')
#ax.annotate(f'{1/m3[0]:.2f}'+r'$\tau$',xy=(-0.5,-2), fontsize='20',color='0.85')
#plt.ylabel(r'$ln(h_r/H)$', fontsize='25')
#plt.xlabel(r'$t/\tau$', fontsize='25')
#print(m1)
plt.savefig('timescales_fast.png', bbox_inches='tight', pad_inches=0.0, dpi=300)
plt.show()


