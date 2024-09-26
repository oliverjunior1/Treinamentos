# import pandas as pd
#
# data = {
#     'calories':[420,380,390],
#     'duration':[50,40,45]
# }
# df = pd.DataFrame(data)
# print(df)
################################################
# import pandas as pd
#
# data = pd.DataFrame({
#     'calories':[420,380,390],
#     'duration':[50,40,45]
# })
#
# print(data)
################################################
import pandas as pd

data = {
    'calories':[420,380,390],
    'duration':[50,40,45]
}
df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df)