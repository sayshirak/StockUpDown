# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pylab import mpl

def onMotion(event):
   #获取鼠标位置和标注可见性
    x = event.xdata
    y = event.ydata
    visible = annot.get_visible()
    if event.inaxes == ax:
    #测试鼠标事件是否发生在曲线上

        contain = Cure.contains(event)
        if contain:
             #设置标注的终点和文本位置,设置标注可见
            annot.xy =(x,y)
            annot.set_text(str(y))#设置标注文本
            annot.set_visible(True)#标注可见
        else:
             #鼠标不在曲线附近,设置标注为不可见
            if visible:
                annot.set_visible(False)
        event.canvas.draw_idle()

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

dfSZZS = pd.read_csv('SZZS.csv')
dfDJI = pd.read_csv('DJI.csv')
totalSZZSCount = 0
SZZSScatter = []
SZZScount = 0
totalDJICount = 0
DJIcount = 0

dfSZZS = dfSZZS.drop(['Open','Close'],axis=1)

for i in range(dfSZZS.shape[0]):
    if dfSZZS.iloc[i,1] == '#VALUE!':
        continue
    else:
        totalSZZSCount += 1
    if abs(float(dfSZZS.iloc[i,1])) >= 0.05:
        SZZScount += 1
        SZZSScatter.append([dfSZZS.iloc[i,0],dfSZZS.iloc[i,1]])
SZZSScatter = np.asarray(SZZSScatter)
#将str类型的数据转换为datetime.date类型的数据，作为x坐标，这样不会出现排序混乱的问题
dt = [datetime.strptime(d, '%Y/%m/%d').date() for d in SZZSScatter[0:,0]]


#纵轴刻度
#plt.ylim(0,100)
#plt.yticks([0,2,4,6,7,10], ['0', '2B', '4B', '8B', '10B'])
#plt.yticks(np.arange(-1, 2, step=0.1))
#plt.grid(True)

fig = plt.figure(figsize=(20,10))
ax = fig.gca()
#坐标轴标签
annot= ax.annotate("",xy=(0,0),xytext=(20,20))#,textcoords='offfset points',bbox=dict(boxstyle='round',fc='w',),arrowprops=dict(arrowstyle='->'))
annot.set_visible(False)
Cure = plt.scatter(dt, SZZSScatter[0:,1],  color='black')
plt.plot(dt, SZZSScatter[0:,1], color='blue', linewidth=3)
fig.canvas.mpl_connect( 'motion_notify_event', onMotion)
plt.xlabel('日期',color='g')
plt.ylabel('涨跌幅',color='g')
plt.show()

print('SZZScount: %d'% SZZScount)
print('totalSZZSCount: %d'% totalSZZSCount)
print('上证指数从1990-12-19到2019-4-9，涨跌幅超过0.01的比例: %4.12f' % (SZZScount/totalSZZSCount))
print('我是分割线=====================================\n')












dfDJI = dfDJI.drop(['Open','Close'],axis=1)
for i in range(dfDJI.shape[0]):
    if dfDJI.iloc[i,1] == '#VALUE!':
        continue
    else:
        totalDJICount += 1
    if abs(float(dfDJI.iloc[i,1])) >= 0.01:
        DJIcount += 1
print('SZZScount: %d'% DJIcount)
print('totalSZZSCount: %d'% totalDJICount)
print('道琼斯指数从1990-12-19到2019-4-9，涨跌幅超过0.01的比例: %4.12f' % (DJIcount/totalDJICount))

'''
dfSZZS = pd.DataFrame(get_price(index[0], start_date='1990-01-01', end_date='2019-09-09', fields=param))
dfSZZS.to_csv('SZZS.csv')
totalCount = dfSZZS.shape[0]
count = 0
print('totalCount: %d'% totalCount)
#print('===========')
for i in range(dfSZZS.shape[0]):
    if abs((dfSZZS.iloc[i,1]-dfSZZS.iloc[i,0])/dfSZZS.iloc[i,0]>= 0.01):
        count += 1
print('count: %d'% count)
print(count/totalCount)

'''

