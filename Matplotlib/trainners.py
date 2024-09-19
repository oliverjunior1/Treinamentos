#----------------pyplot----------------
# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([0,6])
# ypoints = np.array([0,250])
#
# plt.plot(xpoints, ypoints)
# plt.show()
########################################
#------------------ploting----------------
# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([1,8])
# ypoints = np.array([3,10])
#
# plt.plot(xpoints, ypoints)
# plt.show()
#########################################
#-----------------markers-------------------
# import matplotlib.pyplot as plt
# import numpy as np
#
# y = np.array([3,8,1,10])
#
# plt.plot(y, marker = 'o')
# plt.show()
#------------------Line---------------------
# import matplotlib.pyplot as plt
# import numpy as np
#
# y = np.array([3,8,1,18])
#
# plt.plot(y, linestyle = 'dotted')
#
# plt.show()
#-------------------Labels------------------
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.plot(x, y)
#
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.show()
#---------------------------------------Grid------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
#
# plt.grid()
#
# plt.show()
#-----------------------Subplot------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])
#
# plt.subplot(1,2,1)
# plt.plot(x, y)
#
# x = np.array([0,1,2,3])
# y = np.array([10,20,30,40])
#
# plt.subplot(1,2,2)
# plt.plot(x, y)
#
# plt.show()
#------------------------Scatter----------------------------------------
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,5,4,8,9,10,15,11,12])
y = np.array([20,22,21,25,21,24,26,27,28,29,30])

plt.scatter(x, y)
plt.show()
