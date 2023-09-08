##this code generates subfigures S3 b,d and f

import matplotlib.pyplot as plt
import numpy as np

x1,y1 = np.loadtxt('free_copper_gel_38.csv',delimiter=',',unpack=True) #free copper in gel at t=38\tau obtained from phi_o.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 
#x1,y1 = np.loadtxt('free_copper_gel_23.csv',delimiter=',',unpack=True)
#x1,y1 = np.loadtxt('free_copper_gel_9.csv',delimiter=',',unpack=True)
x2,y2 = np.loadtxt('free_copper_sup_38.csv',delimiter=',',unpack=True)#free copper in supernatant at t=38\tau obtained from phi_a.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0
#x2,y2 = np.loadtxt('free_copper_sup_23.csv',delimiter=',',unpack=True)
#x2,y2 = np.loadtxt('free_copper_sup_9.csv',delimiter=',',unpack=True)
x7,y7 = np.loadtxt('free_acid_gel_38.csv',delimiter=',',unpack=True)#free acid in gel at t=38\tau obtained from phi_o_hcl.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 
#x7,y7 = np.loadtxt('free_acid_gel_23.csv',delimiter=',',unpack=True)
#x7,y7 = np.loadtxt('free_acid_gel_9.csv',delimiter=',',unpack=True)
x8,y8 = np.loadtxt('free_acid_sup_38.csv',delimiter=',',unpack=True)#free acid in supernatant at t=38\tau obtained from phi_a_hcl.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 
#x8,y8 = np.loadtxt('free_acid_sup_23.csv',delimiter=',',unpack=True)
#x8,y8 = np.loadtxt('free_acid_sup_9.csv',delimiter=',',unpack=True)

x2 = 2-x2
x8 = 2-x8
fig,ax = plt.subplots(figsize=(20,7.5))

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=32)#labelcolor = "white"

#tick labels
ax.xaxis.set_ticks(np.arange(0.,2.1,1))
ax.yaxis.set_ticks(np.arange(0.,0.0011,0.0005))
ax.xaxis.set_ticklabels(('0', '1', r'$\alpha$'))

#plotting bound copper
ax.plot(x1,y1,color="black",linewidth=4,zorder=2.5)
ax.plot(x2,y2,color="black",linewidth=4,zorder=2.5)
ax.plot(x7,y7,color="magenta",linewidth=4,zorder=2.5)
ax.plot(x8,y8,color="magenta",linewidth=4,zorder=2.5)

ax.set_ylim(-0.0001,0.0011)
ax.set_xlim(0.,2.05)
plt.title(r'$38 \tau$', fontsize=32)
#plt.title(r'$23 \tau$', fontsize=32)
#plt.title(r'$9 \tau$', fontsize=32)
plt.axvline(x=1, color='0.5', linestyle='dashed', linewidth=4)
plt.savefig('free_ions_suppl_weak_38.png', dpi=300)
#plt.savefig('free_ions_suppl_weak_23.png', dpi=300)
#plt.savefig('free_ions_suppl_weak_9.png', dpi=300)
plt.show()
