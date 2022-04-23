#바이올린플롯
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

fish_multi = pd.read_csv("./data/3-3-2-fish_multi_2.csv")
print(fish_multi)

sns.violinplot(data = fish_multi, x = "species",y = "length", color = "blue")
pit.savefig("violinplot")
plt.show()
