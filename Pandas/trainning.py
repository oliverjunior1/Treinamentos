#-------------Series---------------------
# import pandas as pd
#
# a = pd.Series([1,7,2])
#
# print(a)
#----------------------------------------
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index=['x', 'y', 'z'])

print(myvar)

#-----------------------------------------
import pandas as pd

calories = {'day1':420, 'day2':380, 'day3': 390}

myvar = pd.Series(calories)

print(myvar)
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