#대표값
import numpy as np
import scipy as sp

fish_data = np.array([2,3,3,4,4,4,4,6,7,16])
print(np.mean(fish_data))
print("최대값 :{}, 최소값 :{}".format(np.max(fish_data), np.min(fish_data)))
print("중간값 : ",np.median(fish_data))

from scipy import stats
fish_data = np.array([1,2,3,4,5,6,7,8,9,])
print(stats.scoreatpercentile(fish_data, 25))
print(stats.scoreatpercentile(fish_data, 75))

#상위 25퍼센트 평균값을 구한뒤 평균값과 비교해서 S, F 나누기
scores = np.array([80, 79, 76, 50 ,66 ,86 ,100, 40, 60, 50])
cut_score = stats.scoreatpercentile(scores, 75)
print(cut_score)


grade_dic = {}
for score in scores:
    if score >= cut_score:
        grade_dic[score] = "S"
    else:
        grade_dic[score] = "F"
print(grade_dic)


