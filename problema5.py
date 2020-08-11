from scipy import signal
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

if __name__ == "__main__":
    fs, data = wav.read ('audio.wav')
    n = np.arange (0, 143360)
    A = np.array ([1])
    B = np.array ([1, 0.5])
    x = data.T[0]
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

