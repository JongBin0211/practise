#산포도
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

cov_data = pd.read_csv("./data/3-2-3-cov.csv")
print(cov_data)
print(type(cov_data))
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# #콜론값 구하기
# print(cov_data.columns)
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# #인덱스 구조(0부터 10까지 있고 1씩 증가한다)
print(cov_data.index)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
x = cov_data["x"]
y = cov_data["y"]
#타입 알아보기
# print(type(x))
#상관관계 구하기
import scipy as sp
scipy_cov = sp.cov(x, y, ddof = 1)
print(scipy_cov)
#피어슨 상관계수 ( 분산을 1로 만들기)
corre = sp.corrcoef(x, y, ddof = 1)
print(corre)
#두개의 상관관계를 가지고 그림그리기
sns.jointplot(x =  "x", y = "y", data = cov_data, color = "black")
plt.show()