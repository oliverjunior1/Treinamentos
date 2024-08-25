# import pandas as pd
#
# x = pd.read_csv('Pokemon.csv')
#
# print(x)
####################################################################################
# import pandas as pd
#
# print(pd.options.display.max_rows)
##########################################
import pandas as pd

pd.options.display.max_rows = 9999
df = pd.read_csv('Pokemon.csv')

print(df)
