##this code generates subfigures S2 d,e and f

import matplotlib.pyplot as plt
import numpy as np

x1,y1 = np.loadtxt('bound_copper_9_slow.csv',delimiter=',',unpack=True) #bound copper at t=9\tau obtained from phi_b.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 
#x1,y1 = np.loadtxt('bound_copper_23_slow.csv',delimiter=',',unpack=True) #bound copper at t=23\tau obtained from phi_b.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 
#x1,y1 = np.loadtxt('bound_copper_38_slow.csv',delimiter=',',unpack=True) #bound copper at t=38\tau obtained from phi_b.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 
x4,y4 = np.loadtxt('bound_acid_9_slow.csv',delimiter=',',unpack=True) #bound acid at t=9\tau obtained from phi_b_hcl.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 
#x4,y4 = np.loadtxt('bound_acid_23_slow.csv',delimiter=',',unpack=True) #bound acid at t=23\tau obtained from phi_b_hcl.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 
#x4,y4 = np.loadtxt('bound_acid_38_slow.csv',delimiter=',',unpack=True) #bound acid at t=38\tau obtained from phi_b_hcl.pvd(weak_acid_1D_step_2.py) for weak acid using Paraview 5.7.0 

fig,ax = plt.subplots(figsize=(10,7.5))

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=32)#labelcolor = "white"

#tick labels
ax.xaxis.set_ticks(np.arange(0.,1.1,0.2))
ax.yaxis.set_ticks(np.arange(0.,0.04,0.018))

#plotting bound copper
ax.plot(x1,y1,color="black",linewidth=4)
ax.plot(x4,y4,color="magenta",linewidth=4)


ax.set_ylim(-0.001,0.04)
ax.set_xlim(0.,1.05)




#ax.legend()
#ax2.legend()
plt.title(r'$9.0 \tau$', fontsize=32)
#plt.title(r'$23.0 \tau$', fontsize=32)
#plt.title(r'$38.0 \tau$', fontsize=32)
plt.savefig('bound_ions_suppl_slow_9.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
#plt.savefig('bound_ions_suppl_slow_23.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
#plt.savefig('bound_ions_suppl_slow_38.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.show()
