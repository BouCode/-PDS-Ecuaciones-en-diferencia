from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

if __name__ == '__main__':
    n_min, n_max = 0, 100
    n = np.arange (n_min, n_max)
    A = np.array ([1, 0, 0.5])
    B = np.array ([1, -2])
    M = 1;
    f = 2;
    Ts  = 0.025;
    for i in range (len (n)):
        x = M * math.cos (2 * math.pi * f * Ts * i) *np.append(1, np.ones(len(n)-1))
    y = signal.lfilter (B, A, x)
    fig, axs = plt.subplots (2, 1)
    axs[0].stem (n, x)
    axs[0].set_xlabel ('n')
    axs[0].set_ylabel ('x[n]')
    axs[0].set_title ('Entrada')
    axs[1].stem (n, y)
    axs[1].set_xlabel ('n')
    axs[1].set_ylabel ('y[n]')
    axs[1].set_title ('Salida')
    plt.show()