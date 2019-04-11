from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

if 1: # picking on a scatter plot (matplotlib.collections.RegularPolyCollection)
    x, y, c, s = rand(4, 4)
    def onpick3(event):
        ind = event.ind
        print('onpick3 scatter: ' % ind, np.take(['2019-01-02','2019-02-02','2019-03-02','2019-04-02'], ind),
              np.take([0,1,2,3], ind))
    fig = figure()
    col = plt.scatter(['2019-01-02','2019-02-02','2019-03-02','2019-04-02'], [0,1,2,3], color='yellow', picker=True)
    cure = plt.plot(['2019-01-02','2019-02-02','2019-03-02','2019-04-02'], [0,1,2,3], color='blue', linewidth=3)
    #fig.savefig('pscoll.eps')
    fig.canvas.mpl_connect('pick_event', onpick3)
show()