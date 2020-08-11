from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math 

if __name__ == '__main__':
    n = np.arange (-10, 100)
    A = np.array ([1, -1.8 * math.cos ( math.pi/16), 0.81])
    B = np.array ([1, 0.5])
    zeros = np.zeros (len(n))
    zeros [10] = 1
    zeros [11] = 0.5
    y = signal.lfilter(B, A, zeros)
    fig, axs = plt.subplots (2, 1)
    axs[0].stem (n, zeros)
    axs[0].set_xlabel ('n')
    axs[0].set_ylabel ('x[n]')
    axs[0].set_title ('Entrada')
    axs[1].stem (n, y)
    axs[1].set_xlabel ('n')
    axs[1].set_ylabel ('y[n]')
    axs[1].set_title ('Salida')
    plt.show()
