#박스플롯
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

fish_multi = pd.read_csv("./data/3-3-2-fish_multi_2.csv")
print(fish_multi)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

#sns.boxplot(data = fish_multi)
#plt.show()

fish_a = (fish_multi[fish_multi["species"] == "A"])
print(fish_a)
fish_b = fish_multi.query("species == 'B'")
print(fish_b)

sns.boxplot(data = fish_a)
plt.savefig("fish_a")
plt.show()
