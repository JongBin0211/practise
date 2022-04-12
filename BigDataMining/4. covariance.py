#공분산
import pandas as pd
import numpy as np
con_data = pd.read_csv("./data/3-2-3-cov.csv")
print(con_data)

print(con_data["x"])

x = con_data["x"]
y = con_data["y"]

N = len(con_data)
print(N)
#평균값
mu_x = np.mean(x)
mu_y = np.mean(y)

print("x 변수의 평균 : ",mu_x)
print("y 변수의 평균 : ",mu_y)

con_sample = np.sum((x - mu_x)*(y-mu_y))/N
print(" x - y의 공분산:", con_sample)
con_sample1 = np.sum((x - mu_x)*(y-mu_y))/(N-1)
print(" x - y의 불편 공분산:", con_sample1)

con_variance = np.cov(x, y, ddof = 0 )
print(con_variance)
# 공분산은 6.906
# 3.2816은 x 값 분산
# 25.24은 y 값 분산
# ddof 1을 넣으면 불편 공분산
con_variance1 = np.cov(x, y, ddof = 1 )
print(con_variance1)

#피어슨 상관 계수
sigma_2_x = np.var(x, ddof = 1)
sigma_2_y = np.var(y, ddof = 1)
print(sigma_2_x, sigma_2_y)

pi_convar = np.corrcoef(x, y)
print(pi_convar)
# 두개 공분산 값 0.7592
# x 분산 1 y 분산 1
