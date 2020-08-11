from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math 

if __name__ == '__main__':
    n_min, n_max = -10, 50
    T = int ( input ('Ingrese el valor de T: '))
    n = np.arange (n_min, n_max)
    A = np.array ([1])
    p1 = np.array([])
    q1 = np.array([])
    for i in range (n_min, n_max):
        p = T * i + 2 * T
        q = T * i - 5 * T
        p1 = np.append (p1, p)
        q1 = np.append (q1, q)
    k = len(q1)    
    B = p1

    x1 = np.append(np.zeros (10), 1)
    x = np.append (x1, np.zeros (49))
    
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