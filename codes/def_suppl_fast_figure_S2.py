##generates subfigure S2a

import matplotlib.pyplot as plt
import numpy as np

x1,y1 = np.loadtxt('def_0.1.csv',delimiter=',',unpack=True) #u_z at t=0.1\tau obtained from deform.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
x2,y2 = np.loadtxt('def_0.3.csv',delimiter=',',unpack=True) #u_z at t=0.3\tau obtained from deform.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
x3,y3 = np.loadtxt('def_0.5.csv',delimiter=',',unpack=True) #u_z at t=0.5\tau obtained from deform.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
x4,y4 = np.loadtxt('def_0.75.csv',delimiter=',',unpack=True) #u_z at t=0.75\tau obtained from deform.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
x5,y5 = np.loadtxt('def_1.csv',delimiter=',',unpack=True) #u_z at t=1\tau obtained from deform.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
x6,y6 = np.loadtxt('def_2.csv',delimiter=',',unpack=True) #u_z at t=2\tau obtained from deform.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
x7,y7 = np.loadtxt('def_4.csv',delimiter=',',unpack=True) #u_z at t=4\tau obtained from deform.pvd(strog_acid_1D.py) for strong acid using Paraview 5.7.0 
fig,ax = plt.subplots(figsize=(10,7.5))

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=32)#labelcolor = "white"

#tick labels
ax.xaxis.set_ticks(np.arange(0.,1.1,0.2))
ax.yaxis.set_ticks([-0.095, -0.05, 0.0, 0.01])

#plotting bound copper
ax.plot(x1,y1,linewidth=4,label=r'$0.1\tau$')
ax.plot(x2,y2, linewidth=4,label=r'$0.3\tau$')
ax.plot(x3,y3, linewidth=4,label=r'$0.5\tau$')
ax.plot(x4,y4, linewidth=4,label=r'$0.75\tau$')
ax.plot(x5,y5, linewidth=4,label=r'$1\tau$')
ax.plot(x6,y6, linewidth=4,label=r'$2\tau$')
ax.plot(x7,y7, linewidth=4,label=r'$4\tau$')

ax.set_ylim(-0.0995,0.04)
ax.set_xlim(0.,1.05)
ax.legend(loc='upper center', ncol=4,fontsize=20)
plt.savefig('def_suppl_fast_legend.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.show()
