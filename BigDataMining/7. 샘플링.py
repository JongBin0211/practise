#샘플링
import numpy as np
#낱개
data = np.array([1,2,3,4,5,6])
print(data)
#리플레이스 트루는 복원추출(뽑았던 숫자가 다시 나올 수 있음)
one = np.random.choice(data, size = 1, replace = True)
print(one)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in range(len(data)):
    one = np.random.choice(data, size = 1, replace = False)
    print(one)
