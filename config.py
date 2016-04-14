x_min=0
x_max=pi
a_move=2
def u0(x):
    return sin(x)
def uL(t):
    return sin(-a_move*t)
def ua(x,t):
    return sin(x-a_move*t)
