##this code generates subfigure 2b. Here "fast" also means strong acid delivery

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

x1,y1 = np.loadtxt('fast_kf_4_19_K_1000_vc_1_eta_0.225_bound_copper_cu_gel_0.6_refined_mesh.txt',unpack=True) #output of the strong_acid_1D.py, total bound copper in 1D gel
x2,y2 = np.loadtxt('rvalue.csv',delimiter=',',unpack=True) #experimental rvalues of the hydrogel for addition of 1M acid
x30,y30 = np.loadtxt('bound_copper_avg_fast_0.txt', unpack=True)#average bound copper vs time generated for t=0 to 1.0 using bound_copper_avg_strong_2D.nb
x31,y31 = np.loadtxt('bound_copper_avg_fast_1.txt', unpack=True)#average bound copper vs time generated for t=1.1 to 2.0 using bound_copper_avg_strong_2D.nb
x32,y32 = np.loadtxt('bound_copper_avg_fast_2.txt', unpack=True)#average bound copper vs time generated for t=2.1 to 3.0 using bound_copper_avg_strong_2D.nb
x33,y33 = np.loadtxt('bound_copper_avg_fast_3.txt', unpack=True)#average bound copper vs time generated for t=3.1 to 4.0 using bound_copper_avg_strong_2D.nb
x34,y34 = np.loadtxt('bound_copper_avg_fast_4.txt', unpack=True)#average bound copper vs time generated for t=4.1 to 5.0 using bound_copper_avg_strong_2D.nb
x35,y35 = np.loadtxt('bound_copper_avg_fast_5.txt', unpack=True)#average bound copper vs time generated for t=5.1 to 6.0 using bound_copper_avg_strong_2D.nb
x36,y36 = np.loadtxt('bound_copper_avg_fast_6.txt', unpack=True)#average bound copper vs time generated for t=6.1 to 7.0 using bound_copper_avg_strong_2D.nb
x37,y37 = np.loadtxt('bound_copper_avg_fast_7.txt', unpack=True)#average bound copper vs time generated for t=7.1 to 8.0 using bound_copper_avg_strong_2D.nb
x38,y38 = np.loadtxt('bound_copper_avg_fast_8.txt', unpack=True)#average bound copper vs time generated for t=8.1 to 9.0 using bound_copper_avg_strong_2D.nb
x39,y39 = np.loadtxt('bound_copper_avg_fast_9.txt', unpack=True)#average bound copper vs time generated for t=9.1 to 10.0 using bound_copper_avg_strong_2D.nb
x310,y310 = np.loadtxt('bound_copper_avg_fast_10.txt', unpack=True)#average bound copper vs time generated for t=10.1 to 11.0 using bound_copper_avg_strong_2D.nb
x311,y311 = np.loadtxt('bound_copper_avg_fast_11.txt', unpack=True)#average bound copper vs time generated for t=11.1 to 12.0 using bound_copper_avg_strong_2D.nb

x3 = np.concatenate((x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x310,x31))
y3 = np.concatenate((y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y310,y31))
y2 = (y2-162.496)*(0.018/(106.351-162.496))
x2 = x2/2.5


fig,ax = plt.subplots(1,1,figsize=(6.4,4.8))
fig.subplots_adjust(left=0.16)

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)


ax.plot(x3,y3, color='blue', linewidth=5, zorder=2)
ax.scatter(x2,y2+5e-7,marker="o",s=140,color="black", zorder=2.5, facecolor='none', linewidth=3)
ax.plot(x1,y1,color="black",linewidth=5, zorder=2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=32)


#tick labels
ax.xaxis.set_ticks(np.arange(0.,12.1,4))
ax.yaxis.set_ticks(np.arange(0.,0.021,0.01))

ax.set_ylim(-0.001,0.022)
plt.xlim([-1,12.1])
#plt.ylabel(r'$\phi^{(b)}$', fontsize='large', fontweight='bold')
#plt.xlabel(r'$t/\tau$', fontsize='x-large', fontweight='bold')
plt.savefig('rvalue_and_bound_copper_fast_kf_4_19_eta_0.225_cu_gel_0.6.png',dpi=300,bbox_inches='tight', pad_inches=0)
plt.show()
