#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##this note book generates Figure S5


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors


# In[2]:


mesh_size = 12001
timesteps_req = 801


# In[3]:


du_dt = np.zeros((mesh_size,timesteps_req))


# In[4]:


#du_dt for all the time steps exported as csv files from strong_acid_1D/du_dt.pvd using Paraview 5.7.0. It included du_z/dt for all the timesteps. 
for i in range(timesteps_req):
    df = pd.read_csv(f'./du_dt/t_{i}.csv')
    du_dt[:,i] = df["du_dt"].to_numpy()
print(i)


# In[5]:


du_dt = du_dt[1:,84:]


# In[6]:


y_grid = df["Points:0"].to_numpy()[1:]


# In[7]:


x_grid = np.arange(0.84,8.01,0.01)


# In[8]:


X_grid, Y_grid = np.meshgrid(x_grid, y_grid)


# In[9]:


phi_b_hcl_grad = np.zeros((mesh_size, timesteps_req))


# In[10]:


#BBBBound acid gradient for all the time steps exported as csv files from strong_acid_1D/phi_b_hcl.pvd using Paraview 5.7.0. It contains d(phi_b^hcl)/dz for all the time steps
for i in range(timesteps_req):
    df = pd.read_csv(f'./bound_acid_gradient/t_{i}.csv')
    phi_b_hcl_grad[:,i] = df["Result"].to_numpy()


# In[11]:


phi_b_hcl_grad = phi_b_hcl_grad[1:,84:]


# In[12]:


phi_b_grad = np.zeros((mesh_size, timesteps_req))


# In[13]:


#BBBBound copper gradient for all the time steps exported as csv files from strong_acid_1D/phi_b.pvd using Paraview 5.7.0. It contains d(phi_b)/dz for all the time steps
for i in range(timesteps_req):
    df = pd.read_csv(f'./bound_copper_gradient/t_{i}.csv')
    phi_b_grad[:,i] = df["Result"].to_numpy()


# In[14]:


phi_b_grad = phi_b_grad[1:,84:]


# In[15]:


bound_grad_tot_contr = np.divide(phi_b_grad+phi_b_hcl_grad, du_dt) 


# In[18]:


fig, ax = plt.subplots(figsize=(15,10))
pcm = ax.pcolormesh(X_grid, Y_grid, bound_grad_tot_contr, norm=colors.SymLogNorm(linthresh=0.01,linscale=0.1,vmin=-1e-3,vmax=1))
ax.tick_params(axis="x",direction="out", length=10, width=2, labelsize=20)
ax.tick_params(axis="y",direction="out", length=10, width=2, labelsize=20)
ax.set_xticks((0.84,2,4,6,8))
ax.set_yticks((0.000083,0.2,0.4,0.6,0.8,1.0),['0.000083','0.2','0.4','0.6','0.8','1.0'])
#ax.set_xlim(0.84,0.86)
cbar = fig.colorbar(pcm, location="right")
cbar.ax.set_ylabel(r'$\left(\gamma\frac{\partial{\phi^{(b)}}}{\partial{z}} + \chi\frac{\partial{\phi^{(b)}_{HCl}}}{\partial{z}}\right)/\frac{\partial{u}}{\partial{t}}$', fontsize=25)
cbar.ax.tick_params(axis="y",direction="out", length=10, width=2, labelsize=20)
plt.xlabel(r'$t/\tau$', fontsize=25)
plt.ylabel(r'$z/H$', fontsize=25)
plt.savefig('bound_ions_relaxation.png', bbox_inches='tight', pad_inches=0,dpi=300)

