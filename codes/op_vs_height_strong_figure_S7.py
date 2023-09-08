##this code generates subfigure S7a

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

t1, y1 = np.loadtxt('height_fast_eta_0.225_kf_4_19_cu_gel_0.6_refined_mesh.csv', delimiter=',', unpack=True)#height profile generated from deform.pvd which is the output of strong_acid_1D.py using Paraview 5.7.0 
t2, y2 = np.loadtxt('fast_kf_4_19_K_1000_vc_1_eta_0.225_osmotic_pressure_cu_gel_0.6_refined_mesh.txt', unpack=True)#height averaged pressure which is the output of strong_acid_1D.py 


y3 = y1-y1[0]
fig,ax = plt.subplots(1,1,figsize=(6.4,4.8))
fig.subplots_adjust(left=0.16)

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

ax.scatter(y3[0:83],y2[0:83],color="0.5", s=100)
a1 = np.trapz(y2[0:83], y3[0:83])

ax.scatter(y3[83:],y2[83:],color='0.0', s=100)
a2 = np.trapz(y2[83:],y3[83:])

#ax.set_xscale('log')
#ax.set_yscale('log')

ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=32)


ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax.yaxis.set_ticks([0.8,1.2,1.6])
ax.xaxis.set_ticks([0,0.04,0.08])


ax.set_ylim(0.75,1.7)
ax.set_xlim(-0.01,0.09)


#plt.semilogy()
#plt.semilogx()
#ax.legend()
print(a1+a2)
plt.savefig('rel_heigh_vs_osmotic_stress_bnw_fast.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()
