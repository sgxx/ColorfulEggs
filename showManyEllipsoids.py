#coding=utf-8

#@time:2019/3/13 14:56
#@author: Sheng Guangxiao

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time,matplotlib

if __name__ == '__main__':
    values=matplotlib.cm.cmap_d.keys()

    count=0

    length=len(values)

    filepath=r"C:\Users\esa72\PycharmProjects\sgx\Date\201902\CoordTransfer\visualization\image"

    u = np.linspace(0, 2 * np.pi, 1000)
    v = np.linspace(0, np.pi, 1000)

    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 6 * np.outer(np.ones(np.size(u)), np.cos(v))

    for value in values:
        fig=plt.figure()
        ax=fig.gca(projection='3d')

        plt.axis('off')

        plt.plot([-15,0,10],[0,0,0],[0,0,0],color='indigo',linestyle='--')
        plt.plot([0,0,0],[-15,0,10],[0,0,0],color='indigo',linestyle='--')
        plt.plot([0,0,0],[0,0,0],[-10,0,6],color='indigo',linestyle='--')

        ax.plot_surface(x,y,z,cmap=plt.cm.get_cmap(value))

        ax.quiver(0, 0, 6, 0, 0, 5, length=1, color='indigo',linestyle='--')
        ax.quiver(0, 10, 0, 0, 5, 0, length=1, color='indigo',linestyle='--')
        ax.quiver(10, 0, 0, 5, 0, 0, length=1, color='indigo',linestyle='--')

        ax.set_xlim3d(-10,10)
        ax.set_ylim3d(-10,10)
        ax.set_zlim3d(-8,8)

        plt.title(value)
        # plt.show()

        # plt.ion()
        # plt.pause(1.6)
        count+=1
        print(str(count)+"\\"+str(length),value)
        plt.savefig(filepath + "\\" + str(count) + ".png")

        plt.close()
