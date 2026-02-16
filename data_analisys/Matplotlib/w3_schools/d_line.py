import matplotlib.pyplot as plt
import pandas as pd

x = pd.array([0,51,49,42,42,39])
y = pd.array([0,10,15,32,37,42])

plt.plot(x, color='red')
plt.plot(y, color='blue')
plt.xlabel('Lule')
plt.ylabel('Flávio')

plt.show()