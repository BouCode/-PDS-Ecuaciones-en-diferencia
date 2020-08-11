from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math 

if __name__ == '__main__':
    n_min, n_max = 0, 20
    omega = math.pi/4
    n = np.arange (n_min, n_max)
    A = np.array ([1, -5/6, 1/6])
    B = np.array ([0, 1/3])
    xn = np.array([])
    for i in range (0, len (n)):
        xn = np.append (xn, math.cos(omega*i))
    
    dn = np.append(1, np.zeros(len(n)-1))
    y1, y2 = 0, 0
    yn1 = signal.lfilter (B, A, dn, -1)
    yn2 = signal.lfilter (B, A, xn, -1)
    fig, axs = plt.subplots (2, 2)
    axs[0, 0].stem (n, xn)
    axs[0, 0].set_xlabel ('Tiempo n (seg)')
    axs[0, 0].set_ylabel ('Amplitud')
    axs[0, 0].set_title ('Entrada cosenoidal: Cos[omega*n]')
    axs[0, 1].stem (n, yn1)
    axs[0, 1].set_xlabel ('Tiempo n (Seg)')
    axs[0, 1].set_ylabel ('Amplitud')
    axs[0, 1].set_title ('Respuesta impulsional del sistema discreto: h[n]')
    axs[1, 0].stem (n, yn2)
    axs[1, 0].set_xlabel ('Tiempo n (Seg)')
    axs[1, 0].set_ylabel ('Amplitud')
    axs[1, 0].set_title ('Salida: y[n]')
    axs[1, 1].remove()
    plt.show()
