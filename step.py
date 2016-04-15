from useful_features import *
def step_GOD(u_prev,t):
    u_curr=[]
    u_curr.append(uL(t))
    for i in range(1,len(u_prev)):
        u_curr.append((1-q)*u_prev[i]+q*u_prev[i-1])
    return u_curr
def step_LW(u_prev,t)
    u_curr=[]
    u_curr.append(uL(t))
    for i in range(1,len(u_prev)-1):
        u_curr.append((1-q**2)*u_prev[i]+0.5*q(1+q)*u_prev[i-1]-0.5*q(1-q)u_prev[i+1])
    u_curr.append(0)#надо посмотреть что сюда добавить
    return u_curr
def step_DW(u_prev,t):
    a=[]
    b=[]
    c=[]
    d=[]
    a.append(0)
    b.append(1)
    c.append(0)
    d.append(uL(t))
    for i in range(1,len(u_prev)):
        a.append(1-q)
        b.append(q)
        c.append(0)
        d.append(u_prev[i-1])
    return prog(a,b,c,d)
def step_UW(u_prev,t):   
    a=[]
    b=[]
    c=[]
    d=[]
    a.append(0)
    b.append(1)
    c.append(0)
    d.append(uL(t))
    for i in range(1,len(u_prev)):
        a.append(-q)
        b.append(1+q)
        c.append(0)
        d.append(u_prev[i])
    return prog(a,b,c,d)
def step_BAB(u_prev,t):
    a=[]
    b=[]
    c=[]
    d=[]
    a.append(0)
    b.append(1)
    c.append(0)
    d.append(uL(t))
    for i in range(1,len(u_prev)):
        a.append(1-q)
        b.append(1+q)
        c.append(0)
        d.append((1-q)*u_prev[i]+(1+q)*u_prev[i-1])
    return prog(a,b,c,d)
