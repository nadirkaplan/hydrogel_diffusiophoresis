##this code generates subfigures S2 a,b and c

import matplotlib.pyplot as plt
import numpy as np

x1,y1 = np.loadtxt('bound_copper_10.csv',delimiter=',',unpack=True) #bound copper at t=10\tau obtained from phi_b.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
#x1,y1 = np.loadtxt('bound_copper_0.75.csv',delimiter=',',unpack=True) #bound copper at t=0.75\tau obtained from phi_b.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
#x1,y1 = np.loadtxt('bound_copper_0.3.csv',delimiter=',',unpack=True) #bound copper at t=0.3\tau obtained from phi_b.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
x4,y4 = np.loadtxt('bound_acid_10.csv',delimiter=',',unpack=True) #bound acid at t=10\tau obtained from phi_b_hcl.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
#x4,y4 = np.loadtxt('bound_acid_0.75.csv',delimiter=',',unpack=True) #bound acid at t=0.75\tau obtained from phi_b_hcl.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
#x4,y4 = np.loadtxt('bound_acid_0.3.csv',delimiter=',',unpack=True) #bound acid at t=0.3\tau obtained from phi_b_hcl.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 

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
plt.title(r'$10.0 \tau$', fontsize=32)
#plt.title(r'$0.75 \tau$', fontsize=32)
#plt.title(r'$0.3 \tau$', fontsize=32)
plt.savefig('bound_ions_suppl_fast_10.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
#plt.savefig('bound_ions_suppl_fast_0.75.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
#plt.savefig('bound_ions_suppl_fast_0.3.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.show()
