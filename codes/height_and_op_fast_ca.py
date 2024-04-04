##subfigure 2a

import matplotlib.pyplot as plt
import numpy as np

x1,y1 = np.loadtxt('height_fast_ca_varied_acid_front.csv',delimiter=',',unpack=True) #csv file generated from deform.pvd which is the output of strong_acid_1D_ca.py using Paraview 5.7.0 
x3,y3 = np.loadtxt('height_fast_experiments_ca.csv',delimiter=',',unpack=True)#tilt angle profile from experiments
#x2,y2 = np.loadtxt('fast_height_avg_2d.txt', unpack=True, comments='%') #txt file generated from post processing strong_acid_2D.mph in comsol 5.4. In comsol file, Hydrogel height in derivd values.
#x3 = np.array([0,1,2,3])
#y3 = [39.5,32,34.5,39.5]
y3 = np.radians(y3)
y3 = np.cos(y3)
y3 = y3/np.cos(np.radians(9))


fig,ax = plt.subplots(1,1,figsize=(6.4,4.8))
fig.subplots_adjust(left=0.16)

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=32)#labelcolor = "white"

#tick labels
ax.xaxis.set_ticks(np.arange(0.,5.1,2.5))
ax.yaxis.set_ticks([0.78,0.84,0.9])

#plotting experimental data
x3 = x3/2.5
ax.scatter(x3,y3,color="black",marker='o', s=140, zorder=2.5, facecolor='none', linewidth=3)

#plotting 1d gel height

#ax.plot(x2,y2, color='blue', linewidth='5')
ax.plot(x1,y1,color='black',linewidth='5')
ax.set_ylim(0.76,0.92)
ax.set_xlim(-0.4,5.1)

#plt.xlabel(r't/$\tau$', size = 20)
#plt.ylabel(r'$h_r/H$', size = 20)
#ax.set_ylabel(r'$h/H$', fontsize='x-large', fontweight='bold')
#ax.set_xlabel(r'$t/\tau$', fontsize='x-large', fontweight='bold')
#plt.title(r'$\eta = 0.225, \xi_{cu} = 1\times 10^{-10} m^2/s$', fontsize='x-large', fontweight='bold')
plt.savefig('height_fast_ca_varied_acid_front.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.show()
