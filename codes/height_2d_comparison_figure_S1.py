##this code generates figure S1

import matplotlib.pyplot as plt
import numpy as np

x1,y1 = np.loadtxt('height_fast_eta_0.225_kf_4_19_cu_gel_0.6_refined_mesh.csv',delimiter=',',unpack=True)#height profile generated from deform.pvd which is the output of strong_acid_1D.py using Paraview 5.7.0
x3,y3 = np.loadtxt('2d_uniform_signal_height.txt',unpack=True, comments='%')#height profile generated 2D uniaxial deformation. See derived values in strong_acid_2D_uniaxial_def.mph
#x21, y21 = np.loadtxt('nonuniform_fast_height_avg_mod.txt', unpack=True, comments='%')
#x22, y22 = np.loadtxt('nonuniform_fast_height_avg_mod_2.txt', unpack=True, comments='%')
#x23, y23 = np.loadtxt('nonuniform_fast_height_avg_mod_3.txt', unpack=True, comments='%')

#x2 = np.concatenate((x21, x22, x23))
#y2 = np.concatenate((y21, y22, y23))


fig,ax = plt.subplots(1,1,figsize=(6.4,4.8))
fig.subplots_adjust(left=0.16)

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=24)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=24)#labelcolor = "white"

#tick labels
ax.xaxis.set_ticks(np.arange(0.,5.1,1))
ax.yaxis.set_ticks(np.arange(0.9,1.01,0.05))

#plotting experimental data
ax.scatter(x3[:],y3[:],color="black",marker='x', s=160,zorder=2.5, label ='2d uniform')

#plotting 1d gel height

#ax.plot(x2,y2, color='0.8', linewidth='5',label='2d')
ax.plot(x1,y1,color='black',linewidth='5', label='1d uniform')
ax.set_ylim(0.9,1.01)
ax.set_xlim(-0.1,5.1)

plt.legend()
ax.set_ylabel(r'$h/H$', fontsize='x-large', fontweight='bold')
ax.set_xlabel(r'$t/\tau$', fontsize='x-large', fontweight='bold')
#plt.title(r'$\eta = 0.225, \xi_{cu} = 1\times 10^{-10} m^2/s$', fontsize='x-large', fontweight='bold')
plt.savefig('height_2d_1d_comparison.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.show()
