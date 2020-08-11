from scipy import signal 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
import math 

if __name__ == "__main__":
    n_min, n_max = -10, 100
    n = np.arange (n_min, n_max) 
    A = np.array ([1, -1.8 * math.cos(math.pi/16), 0.81])
    B = np.array ([1, -0.5])
    x = 1.5 * np.append (np.zeros(abs(n_min)), np.ones (abs(n_max)))
    y = signal.lfilter (B, A, x)
    fig, axs = plt.subplots (2, 1)
    axs[0].stem (n, x)
    axs[0].set_xlabel ('n')
    axs[0].set_ylabel ('x[n]=1.5*u[n]')
    axs[0].set_title ('Entrada')
    axs[1].stem (n, y)
    axs[1].set_xlabel ('n')
    axs[1].set_ylabel ('y[n]')
    axs[1].set_title ('Salida')
    plt.show()