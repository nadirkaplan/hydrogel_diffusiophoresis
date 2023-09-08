##this code generates subfigure S7b

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

t1, y1 = np.loadtxt('height_slow_eta_0.225_kf_4_19_cu_gel_0.6_step1_refined_mesh.csv', delimiter=',', unpack=True)#height profile generated from deform.pvd which is the output of weak_acid_1D_step_1.py using Paraview 5.7.0 
t3, y3 = np.loadtxt('height_slow_eta_0.225_kf_4_19_cu_gel_0.6_step2_refined_mesh.csv', delimiter=',', unpack=True)#height profile generated from deform.pvd which is the output of weak_acid_1D_step_2.py using Paraview 5.7.0 
t2, y2 = np.loadtxt('slow_kf_4_19_K_1000_vc_1_eta_0.225_cu_gel_0.6_osmotic_pressure_step1_refined_mesh.txt', unpack=True)#height averaged pressure which is the output of weak_acid_1D_step_1.py
t4, y4 = np.loadtxt('slow_kf_4_19_K_1000_vc_1_eta_0.225_osmotic_pressure_cu_gel_0.6_step2_long_refined_mesh.txt', unpack=True)#height averaged pressure which is the output of weak_acid_1D_step_2.py

y11 = y1[0]
y1 = y1-y11
y3 = y3-y11
fig,ax = plt.subplots()


#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)

ax.scatter(y1[0:173],y2[0:173],color="0.5", s=100)
a1 = np.trapz(y2[0:173], y1[0:173])
ax.scatter(y1[173:],y2[173:],color='0.0', s=100)
a2 = np.trapz(y2[173:], y1[173:])
ax.scatter(y3[0:180],y4[0:180],color="0.5", s=100)
a3 = np.trapz(y4[0:180], y3[0:180])
ax.scatter(y3[180:],y4[180:],color="0.0",s=100)
a4 = np.trapz(y4[180:], y3[180:])

ax.set_xscale('log')
#ax.set_yscale('log')

ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=32)


ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_yticks([0.8,1.2,1.6])

ax.set_ylim(0.75,1.7)
ax.set_xlim(0.000009,0.11)


#plt.semilogy()
#plt.semilogx()
#ax.legend()
print(a1+a2+a3+a4)
plt.savefig('rel_heigh_vs_osmotic_stress_bnw_slow_logx.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
plt.show()
