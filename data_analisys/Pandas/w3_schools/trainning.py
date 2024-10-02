#-------------Series---------------------
# import pandas as pd
#
# a = pd.Series([1,7,2])
#
# print(a)
#----------------------------------------
# import pandas as pd
#
# a = [1, 7, 2]
#
# myvar = pd.Series(a, index=['x', 'y', 'z'])
#
# print(myvar)

#-----------------------------------------
# import pandas as pd
#
# calories = {'day1':420, 'day2':380, 'day3': 390}
#
# myvar = pd.Series(calories)
#
# print(myvar)
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
#----------------pandasPlusMatplotlib------------------
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('Pokemon.csv')
#
# df.plot()
# plt.show()
#----------------DataFrames---------------------------
# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df.head(10))
#----------------read_csv-----------------------------
# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df.to_string())
#------------------analize_data-----------------------
# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df.head(10))
#------------------plotting---------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('Pokemon.csv')
#
# df.plot()
#
# plt.show()
#-----------------------pandas---------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
#
# x = pd.DataFrame([1,5,7,8])
# data = plt.plot(x)
#
# plt.show()
#--------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([1,7,8,9])
# y = np.array([3,8,4,10])
# plt.plot(x, y)
#
# plt.show()
#----------------------------------------------------
# import pandas as pd
#
# x = pd.array([1,7,9,6])
#
# y= pd.Series(x)
#
# print(y)
#-----------------------------------------------------
import pandas as pd

x = pd.Series(pd.array([1,2,5,7,10]))

print(x)