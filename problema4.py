import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

if __name__ == "__main__":
    n_min, n_max = 0, 40
    n = np.arange (n_min, n_max)
    h1 = np.array ([])
    h2 = np.array ([])
    for i in range (len(n)):
        h3 = abs ( 0.5**(i/2) * (math.cos (math.pi * i/2) - 2* ((2) ** 0.5) * math.sin (math.pi * i/2)))
        h4 = abs ((0.8 ** i) * (math.cos (math.pi * i/16) + (8.17) * (math.sin (math.pi * i/2))))
        h2 = np.append (h2, h3)
        h1 = np.append (h1, h4)
    fig, axs = plt.subplots (2, 1)
    axs[0].stem (n, h1)
    axs[0].set_xlabel ('n')
    axs[0].set_ylabel ('h1[n]')
    axs[0].set_title ('h1')
    axs[1].stem (n, h2)
    axs[1].set_xlabel ('n')
    axs[1].set_ylabel ('h2[n]')
    axs[1].set_title ('h2')
    sum1, sum2 = sum (h1), sum (h2)
    print (f'Convergencia de h1: {sum1}')
    print (f'Convergencia de h1: {sum2}')
    plt.show()

