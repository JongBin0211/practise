#seaborn_그래프
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

fish_multi = pd.read_csv("./data/3-3-2-fish_multi_2.csv")
print(fish_multi)

fish_multi_group = fish_multi.groupby("species")
print(fish_multi_group)
print(fish_multi_group.describe())
print(fish_multi_group.count())

#데이터분석
want_cols = ["species","length"]
print(fish_multi[want_cols])
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# [][] 이면 행 열 또는 (행,열) 행이 기준일 때 loc 사용
print(fish_multi[1:3]["species"])
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(fish_multi.loc[1:3, "species"])
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

#조건값 a만 보고 싶을 때
print(fish_multi[fish_multi["species"] == "A"])
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(fish_multi[fish_multi.species == "A"])
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# print(fish_multi["species"] == "A") 셀로판지 역할 (A만 나오게)

#A중에 위에 3개만 보고 싶을 때
print(fish_multi[fish_multi.species == "A"][0:3])
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#A 종류에서 3마리의 길이 구하기
# 전체값, 행, 열
print(fish_multi[fish_multi.species == "A"][0:3]["length"])
print(fish_multi[fish_multi.species == "A"].loc[0:3, "length"])
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

print(fish_multi.query("species == 'A'")["length"])