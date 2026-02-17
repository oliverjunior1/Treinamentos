import pandas as pd
import matplotlib.pyplot as plt

x = pd.array([45,39,32])
y = pd.array([10,22,49])

plt.plot(x, color="red", label='Stalinacio')
plt.plot(y, color='blue', label='Flávio')
plt.title("StalinacioxFlávio")
plt.text(1,10,'Crescimento de Flávio do PL', fontsize=12, color="Blue")
plt.show( )