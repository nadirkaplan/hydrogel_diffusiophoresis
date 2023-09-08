#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


sol_vel_x_0 = np.loadtxt('sol_vel_x_weak_0.01.txt', comments='%')
sol_vel_x_1 = np.loadtxt('sol_vel_x_weak_0.05.txt', comments='%')[:,2:]


# In[4]:


sol_vel_x = np.concatenate((sol_vel_x_0,sol_vel_x_1), axis=1)


# In[5]:


sol_vel_x.shape


# In[6]:


np.savetxt('sol_vel_x_weak.txt', sol_vel_x)


# In[7]:


sol_vel_y_0 = np.loadtxt('sol_vel_y_weak_0.01.txt', comments='%')
sol_vel_y_1 = np.loadtxt('sol_vel_y_weak_0.05.txt', comments='%')[:,2:]


# In[8]:


sol_vel_y = np.concatenate((sol_vel_y_0,sol_vel_y_1), axis=1)


# In[9]:


np.savetxt('sol_vel_y_weak.txt', sol_vel_y)


# In[10]:


velocity_y_0 = np.loadtxt('velocity_y_weak_0.01.txt', comments='%')
velocity_y_1 = np.loadtxt('velocity_y_weak_0.05.txt', comments='%')[:,2:]


# In[11]:


velocity_y = np.concatenate((velocity_y_0,velocity_y_1), axis=1)


# In[12]:


np.savetxt('velocity_y_weak.txt', velocity_y)


# In[2]:


velocity_x_0 = np.loadtxt('velocity_x_weak_0.01.txt', comments='%')
velocity_x_1 = np.loadtxt('velocity_x_weak_0.05.txt', comments='%')[:,2:]


# In[3]:


velocity_x = np.concatenate((velocity_x_0,velocity_x_1), axis=1)


# In[4]:


np.savetxt('velocity_x_weak.txt', velocity_x)

