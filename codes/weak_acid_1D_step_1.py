##Code for modeling 1D hydrogel exposed to 0.01M of HCl. Outputs are solutions for various pertinent quantities as pvd files.
##The exclusion radius for steric interactions between Cu2+ ions and polymers is R_e = 4.24*10^-10 m, resulting in eta_DP=eta=R_e^2/(2*k_f)=0.225 with k_f =4*10^-19 m^2.



#importing required libraries

from fenics import*

#import matplotlib.pyplot as plt
#plt.ion()
import sys, math, numpy
from ufl import tanh
import pdb
import numpy as np
from time import perf_counter
from datetime import date


t1_start = perf_counter()

#setting time integration parmeters

T = 8.4   #final time
dt = Constant(1e-4) #initial timestep
dtarray = np.array([]) #array displaying all the timesteps
#dtarray[0] = float(dt) 
dtmax = 1e-4
Nit =1
Nitmax =2
Nitmin = 1



xitemp = 1 #diffusion constant inside the gel
zetatemp = 1 #diffusion constant in the supernatant
phiac = Constant(0.018)
phiac_hcl = Constant(0.036)
r = Constant(1.25*pow(10,4))
gamma = Constant(5.2389)
chi = Constant(2.6194)
omega = Constant(1)
phiac_hcl2 = Constant(0.00006)
ccn = Constant(-1.)
ccn_1 = Constant(0.)
ccn_2 = Constant(0.)
ccn_3 = Constant(0.)
ccn_4 = Constant(0.)
ccr = Constant(1.)
delta = Constant(770)
Hdiff = Constant(750.)
Cudiff = Constant(25.)
cu_gel = Constant(0.6)
phi_p_eq = Constant(0.04)
K = Constant(1000.0)



#defining the mesh
mesh = IntervalMesh(12000,0,1.0)
P1 = FiniteElement('P', mesh.ufl_cell(), 1)
P2 = FiniteElement('P', mesh.ufl_cell(), 2)
element = MixedElement([P1,P1,P1,P1,P1,P1,P1])
V = FunctionSpace(mesh, element)
W = FunctionSpace(mesh, 'P', 1)

v1, v2, v3, v4, v5, v6, v7 = TestFunctions(V)

u = Function(V)
un = Function(V)
un_1 = Function(V)
un_2 = Function(V)
un_3 = Function(V)
un_4 = Function(V)
du = TrialFunction(V)
dv = TrialFunction(V)




u0 = Expression(('-0.0943*x[0]', '0.', '0.', '0.', 'phiac_hcl2*0.5*(1-tanh(125*(x[0]-0.96)))', 'phiac', '0.'), degree=1, phiac = phiac, phiac_hcl2 = phiac_hcl2)
un = interpolate(u0, V)

u1, u2, u3, u4, u5, u6, u7 = split(u); #splitting u
un1, un2, un3, un4, un5, un6, un7 = split(un);
un_11, un_12, un_13, un_14, un_15, un_16, un_17 = split(un_1);
un_21, un_22, un_23, un_24, un_25, un_26, un_27 = split(un_2);
un_31, un_32, un_33, un_34, un_35, un_36, un_37 = split(un_3);
un_41, un_42, un_43, un_44, un_45, un_46, un_47 = split(un_4);

def BDFparameters(nn, ccn, ccn_1, ccn_2, ccn_3, ccn_4, ccr):
    if nn==0:
        ccn.assign(Constant(-1.)); ccr.assign(Constant(1.)); ccn_1.assign(Constant(0.))
        ccn_2.assign(Constant(0.)); ccn_3.assign(Constant(0.)); ccn_4.assign(Constant(0.))                
    elif nn==1:
        ccn.assign(Constant(-4./3.)); ccr.assign(Constant(2./3.)); ccn_1.assign(Constant(1./3.))
        ccn_2.assign(Constant(0.)); ccn_3.assign(Constant(0.)); ccn_4.assign(Constant(0.))
    elif nn==2:
        ccn.assign(Constant(-18./11.)); ccr.assign(Constant(6./11.)); ccn_1.assign(Constant(9./11.))
        ccn_2.assign(Constant(-2./11.)); ccn_3.assign(Constant(0.)); ccn_4.assign(Constant(0.))
    elif nn==3:
        ccn.assign(Constant(-48./25.)); ccr.assign(Constant(12./25.)); ccn_1.assign(Constant(36./25.))
        ccn_2.assign(Constant(-16./25.)); ccn_3.assign(Constant(3./25.)); ccn_4.assign(Constant(0.))
    else:
        ccn.assign(Constant(-300./137.)); ccr.assign(Constant(60./137.)); ccn_1.assign(Constant(300./137.))
        ccn_2.assign(Constant(-200./137.)); ccn_3.assign(Constant(75./137.)); ccn_4.assign(Constant(-12./137.))

def BDFvariables(nn, u, un, un_1, un_2, un_3, un_4):
    if nn==0:
        un.assign(u)    
    elif nn==1:
        un_1.assign(un); un.assign(u)  
    elif nn==2:
        un_2.assign(un_1); un_1.assign(un); un.assign(u)  
    elif nn==3:
        un_3.assign(un_2); un_2.assign(un_1); un_1.assign(un); un.assign(u)  
    else:
        un_4.assign(un_3); un_3.assign(un_2); un_2.assign(un_1); un_1.assign(un); un.assign(u)


def an1(uud):
    return 1./2. *(1+tanh(pow(10,3)*uud))

#definig expressions used in variational form
xi = Constant(xitemp)
zeta = Constant(zetatemp)

n = FacetNormal(mesh)
g1 = (- gamma*u6 -chi*u7)*(1/omega) 
g2 = Constant(0.)
g3 = Constant(0.)
g4 = -xi*Cudiff*cu_gel/(delta)*dot(grad(u2),n)
g5 = -xi*Hdiff/(delta)*dot(grad(u3),n)
g6 = Constant(0.)
g7 = Constant(0.)
eta = Constant(0.225)

boundary_markers = MeshFunction('size_t', mesh, mesh.topology().dim()-1)

class BoundaryX0(SubDomain):
    def inside(self, x, on_boundary):
        return on_boundary and near(x, 0, DOLFIN_EPS)

bx0 = BoundaryX0()
bx0.mark(boundary_markers, 0)

class BoundaryX1(SubDomain):
    def inside(self, x, on_boundary):
        return on_boundary and near(x, 1.0, DOLFIN_EPS)

bx1 = BoundaryX1()
bx1.mark(boundary_markers, 1)
ds = Measure('ds', domain=mesh, subdomain_data=boundary_markers)

#weak statement of the equations

F1 = (u1 + ccn*un1 + ccn_1*un_11 + ccn_2*un_21 + ccn_3*un_31 + ccn_4*un_41)*v1*dx + dt*(ccr*omega*(inner(grad(u1),grad(v1)))*dx + ccr*K*eta*(grad(u2)[0])*v1*dx - ccr*gamma*(grad(u6)[0])*v1*dx - ccr*chi*(grad(u7)[0])*v1*dx - ccr*g1*omega*v1*ds(1))  
F2 = (u2 + ccn*un2 + ccn_1*un_12 + ccn_2*un_22 + ccn_3*un_32 + ccn_4*un_42)*v2*dx + dt*(ccr*xi*Cudiff*cu_gel*(inner(grad(u2),grad(v2)))*dx - ccr*r*u3*u6*v2*dx + ccr*r*u2*(phiac_hcl-2.*u6-u7)*v2*dx  - ccr*g2*v2*ds(0))
F3 = (u3 + ccn*un3 + ccn_1*un_13 + ccn_2*un_23 + ccn_3*un_33 + ccn_4*un_43)*v3*dx + dt*(ccr*xi*Hdiff*(inner(grad(u3),grad(v3)))*dx + ccr*r*u3*(phiac_hcl-u7)*v3*dx - ccr*g3*v3*ds(0))
F4 = (u4 + ccn*un4 + ccn_1*un_14 + ccn_2*un_24 + ccn_3*un_34 + ccn_4*un_44)*v4*dx + dt*(ccr*(zeta*Cudiff/(delta*delta))*(inner(grad(u4),grad(v4)))*dx - ccr*g4*v4*ds(1) - ccr*g6*v4*ds(0))
F5 = (u5 + ccn*un5 + ccn_1*un_15 + ccn_2*un_25 + ccn_3*un_35 + ccn_4*un_45)*v5*dx + dt*(ccr*(zeta*Hdiff/(delta*delta))*(inner(grad(u5),grad(v5)))*dx - ccr*g5*v5*ds(1)- ccr*g7*v5*ds(0))
F6 = (u6 + ccn*un6 + ccn_1*un_16 + ccn_2*un_26 + ccn_3*un_36 + ccn_4*un_46)*v6*dx + dt*(ccr*r*u3*u6*v6*dx - ccr*r*u2*(phiac_hcl-2.*u6-u7)*v6*dx)
F7 = (u7 + ccn*un7 + ccn_1*un_17 + ccn_2*un_27 + ccn_3*un_37 + ccn_4*un_47)*v7*dx - dt*(ccr*r*u3*(phiac_hcl-u7)*v7*dx)


F = F1+F2+F3+F4+F5+F6+F7

#creating a VTK file for visualization output

vtkfile_u1 = File('weak_acid_1D_step_1/deform.pvd')
vtkfile_u2 = File('weak_acid_1D_step_1/phi_o.pvd')
vtkfile_u3 = File('weak_acid_1D_step_1/phi_o_hcl.pvd')
vtkfile_u4 = File('weak_acid_1D_step_1/phi_a.pvd')
vtkfile_u5 = File('weak_acid_1D_step_1/phi_a_hcl.pvd')
vtkfile_u11 = File('weak_acid_1D_step_1/phi_b.pvd')
vtkfile_u12 = File('weak_acid_1D_step_1/phi_b_hcl.pvd')
#vtkfile_u13 = File('osmotic_stress_fast_red_sim_dom_no_du_long_kf_5_19_K33/Pi.pvd')

bc_u1 = DirichletBC(V.sub(0), Constant(0.), bx0) #bottomboundary
#bc_u4 = DirichletBC(V.sub(3), Constant(0.), bx0) #flipped upper boundary
#bc_u5 = DirichletBC(V.sub(4), phiac_hcl2, bx0)


t = 0
nn = 0
pp = -1

net_bound_copper = np.array([])
net_os = np.array([])
net_copper = np.array([])
time = np.array([])


J = derivative(F, u, dv)

while t<T:

    
    if nn%100==0:
        _u1,_u2,_u3,_u4,_u5,_u6,_u7 = un.split()   # saving files
        
        
        vtkfile_u1 << (_u1,t)
        vtkfile_u2 << (_u2,t)
        vtkfile_u3 << (_u3,t)
        vtkfile_u4 << (_u4,t)
        vtkfile_u5 << (_u5,t)
        vtkfile_u11 << (_u6,t)
        vtkfile_u12 << (_u7,t)
        
        #osp = project((K*(_u2 + (1/2)*_u2*_u2 + (1/2)*phi_p_eq*phi_p_eq + phi_p_eq*_u2)), W)
        #osp.rename('osp','osp')
        #vtkfile_u13 << (osp,t)
 
        a1 = assemble(_u6*dx)
        net_bound_copper = np.append(net_bound_copper, float(a1))

        a2 = assemble((-grad(_u1)[0]-chi*_u7-gamma*_u6+K*eta*_u2+K*0.5*phi_p_eq*phi_p_eq)*dx)
        net_os = np.append(net_os, float(a2))
        
        a3 = assemble(_u2*dx)
        net_copper = np.append(net_copper, float(a3))

        time = np.append(time, float(t))

    t  += float(dt)
    
    bc_u2 = DirichletBC(V.sub(1), u(1.0)[3], bx1)
    bc_u3 = DirichletBC(V.sub(2), u(1.0)[4], bx1)
    bcs = [bc_u1,bc_u2,bc_u3]
    
    BDFparameters(nn, ccn, ccn_1, ccn_2, ccn_3, ccn_4, ccr)
    
    problem = NonlinearVariationalProblem(F,u,bcs,J=J)
    solver  = NonlinearVariationalSolver(problem)
    
    
    prm = solver.parameters
    prm['nonlinear_solver']='newton'
    prm["newton_solver"]["absolute_tolerance"]= 1e-12
    prm["newton_solver"]["relative_tolerance"] = 1e-9
    prm["newton_solver"]["maximum_iterations"] = 50
    prm["newton_solver"]["error_on_nonconvergence"]=True
    #prm["newton_solver"]["linear_solver"] = "tfqmr"
    
    solver.solve()
    
    
    
    nn += 1
        
    BDFvariables(nn, u, un, un_1, un_2, un_3, un_4) #updating the variables for next timestep
    
    #if (nn-1)%100 == 0:
        
        #trying to update timestep
        #pp += 1
        #dtarray = np.append(dtarray, float(dt))
        #if dtarray[pp] < (dtmax/2.):
            #dt.assign(Constant(2.*dtarray[pp]))
        #elif dtmax/2. < dtarray[pp] < dtmax:
            #dt.assign(Constant(dtmax))
                
        #(Nit,conv)=solver.solve()
      
           
        #if Nit >= Nitmax:
            #dt.assign(Constant(dtarray[pp]))
        
        
        
        
    
       
    
        
 

t1_end = perf_counter() 
flux_net_bound_copper = np.stack((time, net_bound_copper), axis=-1)
flux_os = np.stack((time, net_os), axis=-1)
flux_copper = np.stack((time, net_copper), axis=-1)
np.savetxt('slow_kf_4_19_K1000_vc_1_eta_0.225_ini_0.96_cu_gel_0.6_step1_refined_mesh.txt', flux_net_bound_copper)
np.savetxt('slow_kf_4_19_K_1000_vc_1_eta_0.225_cu_gel_0.6_osmotic_pressure_step1_refined_mesh.txt', flux_os)
#np.savetxt('copper_vs_time_fast_red_sim_dom_no_du_kf_5_19_K33.txt', flux_copper)
#plt.plot(flux[:,0],flux[:,1])   

File('saved_mesh_step1_refined_mesh.xml') << mesh
File('saved_u_step1_refined_mesh.xml') << un_1
time_data = np.column_stack([t,dt])
np.savetxt("time_step1_refined_mesh.txt", time_data)
print(f"Total runtime in seconds =", t1_end-t1_start)  

pdb.set_trace()
