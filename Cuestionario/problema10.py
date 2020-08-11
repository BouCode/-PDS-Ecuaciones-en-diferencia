from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math 

if __name__ == '__main__':
    n_min, n_max = 0, 51
    n = np.arange (n_min, n_max)
    A = np.array ([1, -1])
    B = np.array ([-5,0,0,0,0,0,0,0,0,4])
    x = np.append(1, np.zeros(len(n)-1))
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