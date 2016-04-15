from step import *
N=101
xn=grid(x_min,x_max,N)
u_a=[u0(x) for x in xn]
u_GOD[u0(x) for x in xn]
u_LW[u0(x) for x in xn]
u_DW[u0(x) for x in xn]
u_UW[u0(x) for x in xn]
u_BAB[u0(x) for x in xn]
t=0
Tau=tau(xn)
t=Tau
while(t<t_max):
    u_GOD=step_COD(u_GOD,t)
    u_LW=step_LW(u_GOD,t)
    u_DW=step_DW(u_GOD,t)
    u_UW=step_UW(u_GOD,t)
    u_BAB=step_BAB(u_GOD,t)
    u_a=[ua(x,t) for x in xn]
