import numpy as np
import math
from scipy.integrate import odeint

def impulse(a, tau, n, inp, duration, c=None):
    def f(y, t):
        dx = y.dot(a.T) / tau
        dx = dx + (inp / tau) if t > 0.05 and t < 0.054 else dx
        return dx

    dt = 1e-3
    n_steps = int(duration / dt) + 1
    ts = np.linspace(0, duration, n_steps)
    xs = odeint(f, np.zeros(n), ts, tcrit=np.linspace(0.04, 0.06, 20))
    return (ts, xs) if c is None else (ts, xs.dot(c.T))

def ou_process(n, dt, tau, duration): 
    t_max = 3 + int(duration / dt)   
    table = np.zeros((t_max, n))
    x = np.random.randn(1,n)
    for i in range(t_max): 
        x = x if (i==0) else ((1 - (dt / tau))* x) + (math.sqrt(2 * dt / tau) * np.random.randn(1,n))
        table[i,:] = x
    return (table, lambda t : table[int(t/dt),:])
