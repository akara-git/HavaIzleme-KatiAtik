# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:05:01 2020

@author: Hp
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data=pd.read_excel("C:/Users/Hp/Desktop/deneme.xlsx")#veriokundu

#veri tipinin floata çevrilmesi
data['PM10'] = data['PM10'].astype('float')
data['SO2'] = data['SO2'].astype('float')
data['HavaSıcaklığı'] = data['HavaSıcaklığı'].astype('float')
data['RüzgarHızı'] = data['RüzgarHızı'].astype('float')
data['BağılNem'] = data['BağılNem'].astype('float')
data['HavaBasıncı'] = data['HavaBasıncı'].astype('float')
data['KabinSıcaklığı'] = data['KabinSıcaklığı'].astype('float')
data['RuzgarYönü'] = data['RuzgarYönü'].astype('float')

data = data.fillna(data.mean())


plt.figure(figsize=(20,12))
plt.subplot(2,2,1)
plt.plot(data.Tarih,data.PM10,color="red")
plt.plot(data.Tarih,data.SO2,color="blue")
plt.plot(data.Tarih,data.HavaSıcaklığı,color="black")
plt.plot(data.Tarih,data.RüzgarHızı,color="orange")
plt.plot(data.Tarih,data.BağılNem,color="gray")
plt.plot(data.Tarih,data.KabinSıcaklığı,color="yellow")
plt.plot(data.Tarih,data.RuzgarYönü,color="magenta")
plt.xlabel("Tarih")
plt.title("Zamana Göre PM10(Red)-SO2(Blue)-HavaSıcaklığı(Black)-RüzgarHızı(Orange)-BağılNem(Gray)-KabinSıcaklığı(Yellow)-RuzgarYönü(magenta) değişimi")

plt.subplot(2,2,2)
plt.plot(data.Tarih,data.HavaBasıncı,color="green")
plt.xlabel("Tarih")
plt.ylabel("Hava Basıncı")
plt.title("Zamana Göre Hava Basıncı değişimi")
plt.show()

sns.scatterplot(x ="SO2",y="PM10", data=data)
plt.show()
sns.scatterplot(x ="HavaSıcaklığı",y="RüzgarHızı", data=data,color="yellow")
plt.show()
sns.scatterplot(x ="HavaSıcaklığı",y="BağılNem", data=data,color="green")
plt.show()
sns.scatterplot(x ="RüzgarHızı",y="RuzgarYönü", data=data,color="red")
plt.show()
sns.distplot(data['PM10'])
sns.pairplot(data)
veri=pd.read_excel("C:/Users/Hp/Desktop/deneme.xlsx",index_col=0)
veri.plot.bar(stacked=True,figsize=(40,12))












