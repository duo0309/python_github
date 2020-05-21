import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

x = np.arange(0,500+1,1)
y = np.log(x)

[plt.plot(x,y+i,'o') for i in range(10)]
plt.show()