# 표본통계
import numpy as nd
import numpy as np
import scipy as sp
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

population = stats.norm(loc=4, scale = 0.8)

x = np.linspace(0, 8, 100)
print(x)
print(population.pdf(4-(0.8*1.96)))
y = population.pdf(x)
plt.plot(x, y)
plt.show()

sample_means_array = np.zeros(10000)
# print(sample_means_array)
population = stats.norm(loc=4, scale=0.8)
np.random.seed(1)

for i in range(0, 10000):
    sample = population.rvs(size=10)
    # sample = population.nean(sample)
# print(sample)
sample_means_array[i] = np.mean(sample)
print(sample_means_array)
print(np.mean(sample_means_array))
