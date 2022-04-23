#모집단에서 샘플링
import numpy as np
import pandas as pd
import scipy as sp
from matplotlib import pyplot as plt
import seaborn as sns

# fish = [2,3,4,5,6] #(낱개)
# print(type(fish))
# print(fish)
# print(fish.shape)
# #랜덤값 고정
# np.random.seed(1)
# fish_5 = np.array([2,3,4,5,6]) #(한 덩어리)
# choise_one = np.random.choice(fish_5,size=3, replace=False) #replace True(뽑았던 숫자 뽑힘), False(뽑았던 숫자 안뽑힘)
# print(choise_one)
# fish_temp = pd.read_csv("./data/3-4-1-fish_length_100000.csv")
# print(type(fish_temp))
# print(len(fish_temp))
# print(fish_temp.head(5))
# print(fish_temp.tail(5))
# print(fish_temp.columns)
# print(fish_temp.index)
# print(fish_temp.values)
# fish_a = fish_temp.values
# print(type(fish_a))
# 모집단의 평균
# print("100000마리의 모집단 평균 : ", np.mean(fish_a))
#############################
# data = pd.read_csv("./data/5-1-1-beer.csv")
# print(data.head(5))
# print(data.columns)
# print(data["temperature"].head(5))
# print(type(data))

# beer_temp = data["temperature"]
# data1 = pd.read_csv("./data/5-1-1-beer.csv")["temperature"]
# print(data1.head(5))
# print("모집단의 평균: ",np.mean(data1))
# print("모집단의 표준분산 : ",np.var(data1)) #(분산은 편차 제곱)
# print("모집단의 표준편차 : ",np.std(data1))
#############################

# print(beer_temp.head(5))
# print(type(beer_temp))
# print(beer_temp.unique())

#물고기 십만마리중 랜덤으로 만마리
fish_length = pd.read_csv("./data/3-4-1-fish_length_100000.csv")
print(type(fish_length))
print(fish_length.head(5)) #앞에서 5개만 추출
fish_val = fish_length.values
fish_sample = np.random.choice(fish_length["length"], size=10000,replace=False)
print(fish_sample)
print("모집단의 표준편자 :",np.std(fish_sample, ddof=0))
print("샘플의 표준편자 :",np.std(fish_sample, ddof=1))
print("샘플의 분산 :",np.var(fish_sample, ddof=1))