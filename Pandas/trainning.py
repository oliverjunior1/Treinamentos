# import pandas as pd
#
# a = pd.Series([1,7,2])
#
# print(a)
#--------------dataframes----------------
# import pandas as pd
#
# data = pd.DataFrame({
#     'calories':[420,380,390],
#     'duration':[50,40,45]
# })
#
# print(data)
#---------------read-csv------------------
# import pandas as pd
#
# pd.options.display.max_rows = 9999
# df = pd.read_csv('Pokemon.csv')
#
# print(df)
#----------------plotting------------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Pokemon.csv')

df.plot()
plt.show()