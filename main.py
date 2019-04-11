# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from pylab import mpl
from matplotlib.pyplot import figure, show

'''
matplotlib日期
https://matplotlib.org/api/dates_api.html#matplotlib.dates.datestr2num
设置matplotlib横坐标为日期格式
https://blog.csdn.net/helunqu2017/article/details/78736686
'''


mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def onMotion(event):
    ind = event.ind
    x = str(np.take(dt, ind)[0].year) + '-' + str(np.take(dt, ind)[0].month) + '-' + str(np.take(dt, ind)[0].day)
    y = np.take(SZZSScatter[0:,1], ind)[0]
    annot= ax.annotate("", xy=(x, float(y)),
                       xytext=(str(x), str(y)), arrowprops=dict(arrowstyle="->"))
    annot.xy =(str(x), str(y))
    annot.set_text((annot.xy))#设置标注文本
    '''
    是否可以在这里直接设置标注
    annot= ax.annotate("", xy=('1990/12/20', y),
                       xytext=('11'), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(True)#标注可见
    '''
    print(x, y)
    event.canvas.draw_idle()

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
    if abs(float(dfSZZS.iloc[i,1])) >= 0.1:
        SZZScount += 1
        SZZSScatter.append([dfSZZS.iloc[i,0],dfSZZS.iloc[i,1]])
SZZSScatter = np.asarray(SZZSScatter)
#将str类型的数据转换为datetime.date类型的数据，作为x坐标，这样不会出现排序混乱的问题
dt = [datetime.strptime(d, '%Y/%m/%d').date() for d in SZZSScatter[0:,0]]
#dt = [ mdates.datestr2num(d) for d in SZZSScatter[0:,0]  ]

#指定绘图板大小
fig = plt.figure(figsize=(15,8))
ax = fig.gca()
#指定横坐标为日期
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
#指定横坐标每一格的单位,使用了自动分配
#也可以使用DayLocator(bymonthday=[1,32])
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
#坐标轴标签
plt.xlabel('日期',color='g')
plt.ylabel('涨跌幅',color='g')
#纵轴刻度
#plt.ylim(-1,2)
#plt.yticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2], [-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2])
#plt.yticks(np.arange(-1, 2, step=0.1))
plt.grid(True)

scatter = plt.scatter(dt, SZZSScatter[0:,1],  color='black',picker=True)
cure = plt.plot(dt, SZZSScatter[0:,1], color='blue', linewidth=3)
#创建标注对象
annot= ax.annotate("",xy=(0, 0), xytext=(0,0), arrowprops=dict(arrowstyle="->"))
annot.set_visible(True)
fig.canvas.mpl_connect( 'pick_event', onMotion)

show()

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

