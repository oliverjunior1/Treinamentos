import pandas as pd
import matplotlib.pyplot as plt

x = pd.array([35,45,15,25,77,99])
y = pd.DataFrame([15,5,25,77,55,15])
plt.plot(x, y, 'o')
plt.show()