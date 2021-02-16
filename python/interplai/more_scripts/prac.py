import datetime
tm=datetime.datetime.fromtimestamp(1603235767).strftime('%Y-%m-%d %H:%M:%S')
print(tm)
import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(5, 4, 1)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 2)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(5, 4, 3)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 4)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(5, 4, 5)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 6)
# plt.plot(x,y)
#
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 7)
# plt.plot(x,y)
#
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 8)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 9)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 10)
# plt.plot(x,y)
#
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 10)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 10)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 10)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 10)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 10)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(5, 4, 10)
# plt.plot(x,y)
#
# plt.show()

fig, axs = plt.subplots(4,4, figsize=(15, 6), facecolor='w', edgecolor='k')
# fig.subplots_adjust(hspace = .5, wspace=.001)
plt.subplots_adjust(left=.0125, right=5, bottom=.1, top=0.9)
plt.subplots_adjust(hspace = .5, wspace=.01)
axs = axs.ravel()

for i in range(10):

    axs[i].scatter(np.random.rand(10,10),np.random.rand(10,10),s=10)
    axs[i].set_title(str(250+i))

plt.tight_layout()

plt.show()