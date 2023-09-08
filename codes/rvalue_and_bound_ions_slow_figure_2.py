#include bound_copper_avg_8.4

import matplotlib.pyplot as plt
import numpy as np

x1,y1 = np.loadtxt('slow_kf_4_19_K1000_vc_1_eta_0.225_ini_0.96_cu_gel_0.6_step1_refined_mesh.txt',unpack=True)#output of weak_acid_1d_step_1.py, total bound copper vs time for addition of 0.01M acid
x4,y4 = np.loadtxt('slow_kf_4_19_K1000_vc_1_eta_0.225_ini_0.96_cu_gel_0.6_step2_long_refined_mesh.txt',unpack=True)#output of weak_acid_1d_step_1.py, total bound copper vs time for addition of 0.01M acid
x2,y2 = np.loadtxt('rvalue_slow.csv',delimiter=',',unpack=True)#tilt angle values for the addition of 0.05M acid
x5,y5 = np.loadtxt('rvalue_slow_1.csv',delimiter=',',unpack=True)#tilt angle values for the addition of 0.01M acid
x30,y30 = np.loadtxt('bound_copper_avg_0.txt', unpack=True)#average bound copper vs time generated for t=0 to 1.0 using bound_copper_avg_weak_2D.nb
x31,y31 = np.loadtxt('bound_copper_avg_1.txt', unpack=True)#average bound copper vs time generated for t=1.1 to 2.0 using bound_copper_avg_weak_2D.nb
x32,y32 = np.loadtxt('bound_copper_avg_2.txt', unpack=True)#average bound copper vs time generated for t=2.1 to 3.0 using bound_copper_avg_weak_2D.nb
x33,y33 = np.loadtxt('bound_copper_avg_3.txt', unpack=True)#average bound copper vs time generated for t=3.1 to 4.0 using bound_copper_avg_weak_2D.nb
x34,y34 = np.loadtxt('bound_copper_avg_4.txt', unpack=True)#average bound copper vs time generated for t=4.1 to 5.0 using bound_copper_avg_weak_2D.nb
x35,y35 = np.loadtxt('bound_copper_avg_5.txt', unpack=True)#average bound copper vs time generated for t=5.1 to 6.0 using bound_copper_avg_weak_2D.nb
x36,y36 = np.loadtxt('bound_copper_avg_6.txt', unpack=True)#average bound copper vs time generated for t=6.1 to 7.0 using bound_copper_avg_weak_2D.nb
x37,y37 = np.loadtxt('bound_copper_avg_7.txt', unpack=True)#average bound copper vs time generated for t=7.1 to 8.0 using bound_copper_avg_weak_2D.nb
x38,y38 = np.loadtxt('bound_copper_avg_8.txt', unpack=True)#average bound copper vs time generated for t=8.1 to 8.4 using bound_copper_avg_weak_2D.nb
x384,y384 = np.loadtxt('bound_copper_avg_8.4.txt', unpack=True)#average bound copper vs time generated for t=8.5 to 9.0 using bound_copper_avg_weak_2D.nb
x39,y39 = np.loadtxt('bound_copper_avg_9.txt', unpack=True)#average bound copper vs time generated for t=9.1 to 10.0 using bound_copper_avg_weak_2D.nb
x310,y310 = np.loadtxt('bound_copper_avg_10.txt', unpack=True)#average bound copper vs time generated for t=10.1 to 11.0 using bound_copper_avg_weak_2D.nb
x311,y311 = np.loadtxt('bound_copper_avg_11.txt', unpack=True)#average bound copper vs time generated for t=11.1 to 12.0 using bound_copper_avg_weak_2D.nb
x312,y312 = np.loadtxt('bound_copper_avg_12.txt', unpack=True)#average bound copper vs time generated for t=12.1 to 13.0 using bound_copper_avg_weak_2D.nb
x313,y313 = np.loadtxt('bound_copper_avg_13.txt', unpack=True)#average bound copper vs time generated for t=13.1 to 14.0 using bound_copper_avg_weak_2D.nb
x314,y314 = np.loadtxt('bound_copper_avg_14.txt', unpack=True)#average bound copper vs time generated for t=14.1 to 15.0 using bound_copper_avg_weak_2D.nb
x315,y315 = np.loadtxt('bound_copper_avg_15.txt', unpack=True)#average bound copper vs time generated for t=15.1 to 16.0 using bound_copper_avg_weak_2D.nb
x316,y316 = np.loadtxt('bound_copper_avg_16.txt', unpack=True)#average bound copper vs time generated for t=16.1 to 17.0 using bound_copper_avg_weak_2D.nb
x317,y317 = np.loadtxt('bound_copper_avg_17.txt', unpack=True)#average bound copper vs time generated for t=17.1 to 18.0 using bound_copper_avg_weak_2D.nb
x318,y318 = np.loadtxt('bound_copper_avg_18.txt', unpack=True)#average bound copper vs time generated for t=18.1 to 19.0 using bound_copper_avg_weak_2D.nb
x319,y319 = np.loadtxt('bound_copper_avg_19.txt', unpack=True)#average bound copper vs time generated for t=19.1 to 20.0 using bound_copper_avg_weak_2D.nb
x320,y320 = np.loadtxt('bound_copper_avg_20.txt', unpack=True)#average bound copper vs time generated for t=20.1 to 21.0 using bound_copper_avg_weak_2D.nb
x321,y321 = np.loadtxt('bound_copper_avg_21.txt', unpack=True)#average bound copper vs time generated for t=21.1 to 22.0 using bound_copper_avg_weak_2D.nb
x322,y322 = np.loadtxt('bound_copper_avg_22.txt', unpack=True)#average bound copper vs time generated for t=22.1 to 23.0 using bound_copper_avg_weak_2D.nb
x323,y323 = np.loadtxt('bound_copper_avg_23.txt', unpack=True)#average bound copper vs time generated for t=23.1 to 24.0 using bound_copper_avg_weak_2D.nb
x324,y324 = np.loadtxt('bound_copper_avg_24.txt', unpack=True)#average bound copper vs time generated for t=24.1 to 25.0 using bound_copper_avg_weak_2D.nb
x325,y325 = np.loadtxt('bound_copper_avg_25.txt', unpack=True)#average bound copper vs time generated for t=25.1 to 26.0 using bound_copper_avg_weak_2D.nb
x326,y326 = np.loadtxt('bound_copper_avg_26.txt', unpack=True)#average bound copper vs time generated for t=26.1 to 27.0 using bound_copper_avg_weak_2D.nb
x327,y327 = np.loadtxt('bound_copper_avg_27.txt', unpack=True)#average bound copper vs time generated for t=27.1 to 28.0 using bound_copper_avg_weak_2D.nb

x3 = np.concatenate((x30,x31,x32,x33,x34,x35,x36,x37,x38,x384,x39,x310,x311,x312,x313,x314,x315,x316,x317,x318,x319,x320,x321,x322,x323,x324,x325,x326,x327))
y3 = np.concatenate((y30,y31,y32,y33,y34,y35,y36,y37,y38,y384,y39,y310,y311,y312,y313,y314,y315,y316,y317,y318,y319,y320,y321,y322,y323,y324,y325,y326,y327))

y2 = (y2-162.496)*(0.018/(106.351-162.496))
y5 = (y5-162.496)*(0.018/(106.351-162.496))

x2 = x2-9
x2 = x2/2.5
x5 = x5/2.5 
x4 = x4 + 8.4
avg_area = 9.603e-4
#y3 = y3/avg_area

fig,ax = plt.subplots()

#axis linewidth
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)
    
ax.plot(x3,y3, color='blue', linewidth=5, zorder=2)
ax.plot(x1,y1,color="black",linewidth=5, zorder=2)
ax.plot(x4,y4,color="black",linewidth=5, zorder=2)

#tick parameters
ax.tick_params(axis="x", direction = "in", length=10, width=2, labelsize=32)
ax.tick_params(axis="y", direction = "in", length=10, width=2, labelsize=0, labelcolor="white")

#tick labels
ax.xaxis.set_ticks(np.arange(0.,28.1,7))
ax.yaxis.set_ticks(np.arange(0.,0.021,0.01))

ax.scatter(x2[::2],y2[::2],marker="o",s=140,color="black", zorder=2.5, facecolor='none',linewidth=3)
ax.scatter(x5[::2],y5[::2],marker="o",s=140,color="black", zorder=2.5,facecolor='none',linewidth=3)

ax.set_ylim(-0.001,0.022)
plt.xlim([-1,28.1])
plt.savefig('rvalue_and_bound_copper_slow_interpolated_stepwise.png',dpi=300,bbox_inches='tight',pad_inches=0.0)
plt.show()
