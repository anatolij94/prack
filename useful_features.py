from config import *
def prog(a, b, c, d):
    ''' Метод прогонки.
    '''
    M = len(d) - 1
    P = [0 for _ in range(M+1)]
    Q = [0 for _ in range(M+1)]
    u = [0 for _ in range(M+1)]

    P[0] = - c[0] / b[0]
    Q[0] = d[0] / b[0]

    for i in range(1, M+1):
        P[i] = - c[i]/(a[i] * P[i-1] + b[i])
        Q[i] = (d[i]-a[i]*Q[i-1])/(a[i]*P[i-1]+b[i])

    u[M] = Q[M]
    for i in range(M-1, -1, -1):
        u[i] = P[i] * u[i+1] + Q[i]

    return u
def grid(left, right, n):
    h = (right - left) / n
    return [left + h * i for i in range(n+1)]
def h(x_array):
    return (x_array[-1]-x_array[0])/(len(x_array)-1)
def tau(x_array):
    return q*h(x_array)/a_move