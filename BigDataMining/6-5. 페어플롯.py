#페어플롯
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

iris = sns.load_dataset("iris")
# print(iris)
# #타입 알아보기
# print(type(iris))
# print(iris.columns)
sns.pairplot(iris, hue = "species", palette = "Blues")
plt.savefig("pairplot")
plt.show()
