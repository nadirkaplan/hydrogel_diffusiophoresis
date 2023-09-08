#this code combines streamplots and deformations.

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
from scipy import interpolate
from scipy.spatial import Delaunay
import numpy as np
from numpy import*
import matplotlib as mpl

def combine(n):
    img1 = plt.imread(f'{n}velocity_strong.png')
    img2 = plt.imread(f'{n}deform_strong.png')
    fig, ax =  plt.subplots(figsize=(12.5,5))

    cmap = mpl.cm.YlOrBr
    norm = mpl.colors.LogNorm(vmin=0.0001, vmax=0.10300605694119168)

    cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), orientation='horizontal', aspect=20, shrink=0.4, pad=0.25)
    cbar.set_ticks([0.0001,0.001,0.01,0.1],labels=[r'$<10^{-4}$',r'$10^{-3}$',r'$10^{-2}$',r'$10^{-1}$'], size=15)
    cbar.set_label(r'$U/ U^{(0)}$', size=15,family='sans-serif')
    ax.imshow(img1,origin='upper',aspect='equal',extent=(0,8000,0,3200))
    ax.imshow(img2, origin='upper', aspect='equal',extent=(0,8000,0,3200))
    ax.set_xticks(np.arange(0,8001,step=1600), ['0', '0.2L', '0.4L', '0.6L', '0.8L', 'L'])
    ax.set_yticks(np.arange(0,3201,step=1600), ['0', '1H', '771H'])
    ax.tick_params(axis="x",direction="inout", length=20, width=2, labelsize=18)
    ax.tick_params(axis="y",direction="inout", length=20, width=2, labelsize=18)
    for axis in  ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(2)
    ax.spines[['right', 'top']].set_visible(False)
    plt.title(f'{n*0.05:.2f}'+r'$\tau$', fontsize=20)
    plt.xlabel('x', fontsize=20)
    plt.ylabel('z', fontsize=20)
    plt.savefig(f'{n}combined_just_strong.png', dpi=300, pad_inches=0, bbox_inches='tight')
    plt.close(fig)
    

for n in range(241):
    combine(n)
