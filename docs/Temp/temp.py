import matplotlib.pyplot as plt
import numpy as np


name = ['sun', 'jupiter', 'earth', 'moon']
volume = [1.41*10**18, 1.43*10**15, 1.83*10**12, 2.20*10**10]

plt.bar(name, [np.log10(i) for i in volume])
plt.title('Log-scale value')

plt.show()