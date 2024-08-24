# import pandas as pd
#
# a = [1,7,2]
#
# x = pd.Series(a)
#
# print(x)
################################################
# import pandas as pd
#
# a = [1,7,2]
#
# x = pd.Series(a, index=['a', 'b', 'c'])
#
# print(x)
################################################
# import pandas as pd
#
# calories = {'day1':420, 'day2':380, 'day3':390}
#
# myvar = pd.Series(calories)
#
# print(myvar)
################################################
# import pandas as pd
#
# calories = {'day1':420, 'day2':380, 'day3':390}
#
# x = pd.Series(calories, index=['day1', 'day2'])
#
# print(x)
################################################
import pandas as pd

x = {
    'calories':[420,380,360],
    'duration':[50,40,45]
}
y = pd.DataFrame(x)

print(y)
