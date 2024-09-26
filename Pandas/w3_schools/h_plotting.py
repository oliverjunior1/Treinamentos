# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('data1.csv')
#
# df.plot()
#
# plt.show()
#####################################
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind='scatter', x='Duration', y='Calories')

plt.show()