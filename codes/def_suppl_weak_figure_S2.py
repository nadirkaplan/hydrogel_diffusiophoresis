##generates subfigure S2b


import matplotlib.pyplot as plt
import numpy as np

x1,y1 = np.loadtxt('def_9.csv',delimiter=',',unpack=True) #u_z at t=9\tau obtained from deform.pvd(weak_acid_1D_step_2.py) for strong acid using Paraview 5.7.0 
x2,y2 = np.loadtxt('def_23.csv',delimiter=',',unpack=True) #u_z at t=23\tau obtained from deform.pvd(weak_acid_1D_step_2.py) for strong acid using Paraview 5.7.0 
x3,y3 = np.loadtxt('def_38.csv',delimiter=',',unpack=True) #u_z at t=38\tau obtained from deform.pvd(weak_acid_1D_step_2.py) for strong acid using Paraview 5.7.0 
x4,y4 = np.loadtxt('def_10.csv',delimiter=',',unpack=True) #u_z at t=10\tau obtained from deform.pvd(weak_acid_1D_step_2.py) for strong acid using Paraview 5.7.0 

fig,ax = plt.subplots(figsize=(10,7.5))

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=0.0, labelcolor = "white")

#tick labels
ax.xaxis.set_ticks(np.arange(0.,1.1,0.2))
ax.yaxis.set_ticks([-0.095, -0.05, 0.0, 0.01])

#plotting bound copper
ax.plot(x1,y1,linewidth=4,label=r'$9\tau$')
ax.plot(x4,y4, linewidth=4,label=r'$10\tau$')
ax.plot(x2,y2, linewidth=4,label=r'$23\tau$')
ax.plot(x3,y3, linewidth=4,label=r'$38\tau$')


ax.set_ylim(-0.0965,0.04)
ax.set_xlim(0.,1.05)
ax.legend(loc='upper center', ncol=4,fontsize=20)
plt.savefig('def_suppl_slow.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.show()
