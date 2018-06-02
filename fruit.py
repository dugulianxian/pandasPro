# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from numpy.random import randn
from pandas import Series

# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
a = pd.read_csv('fruitveg.csv', sep=',')
a2 = a[1:205]  # 选取2004的数据
a3 = a2[14:44]  # 选取Dessert Apples的数据

# 获取索引,drop_duplicates()去重
ListColumn_d = list(a3['Catagries'].drop_duplicates());
ListColumn = list(a3['Catagries']);
del a3['2004']
# 修改index为Catagries列
a4 = a3.set_index('Catagries')
del a4['Quality']
del a4['Units']
print(a4)

df3 = pd.DataFrame(columns=['1st', '2nd', 'Ave'], index=ListColumn_d)


def data_deal(cog, type):
    if type == 'Other Early Season' or type == 'Other Mid Season' or type == 'Other Late Season':
        cog_1st = cog.astype('float').max()
        cog_2nd = cog.astype('float').min()
        cog_Ave = cog.astype('float').mean()
        print('%s' % type + '品种苹果:全年最高销售价' + str(cog_1st) + '平均售价' + str(cog_Ave) + '最低售价' + str(cog_2nd))
    else:
        cog_copy = cog.copy()
        # 改变索引值
        cog_copy.index.values[0] = cog_copy.index.values[0] + '_1st'
        cog_copy.index.values[1] = cog_copy.index.values[1] + '_2nd'
        cog_copy.index.values[2] = cog_copy.index.values[2] + '_Ave'

        # 找出每一行最大值，此处要用astype('float')将字符串转为float再计算，使用'%.2f'保留两位小数
        cog_1st = '%.2f' % cog_copy.loc[cog_copy.index.values[0]].astype('float').max()
        cog_2nd = '%.2f' % cog_copy.loc[cog_copy.index.values[1]].astype('float').min()
        cog_Ave = '%.2f' % cog_copy.loc[cog_copy.index.values[2]].astype('float').mean()
        print('%s' % type + '品种苹果:全年最高销售价' + str(cog_1st) + '平均售价' + str(cog_Ave) + '最低售价' + str(cog_2nd))
        # 定义数据list集合
    # 必须转成float,不然后面调用plot画图要出错
    list = [float(cog_1st), float(cog_Ave), float(cog_2nd)]
    df3.loc['%s' % type] = list


# 处理各个品类的苹果
for x in ListColumn_d:
    print(x)
    cog = a4.loc[x]
    data_deal(cog, x)
print(df3)

# print(type(df3.loc['Cox’s Orange-group','1st']))
# Dessert Apples全年销量统计图
df3.plot(kind='bar', figsize=(10, 10))
plt.title('Dessert Apples All-Year Data')
plt.show()
