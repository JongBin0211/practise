#시각화
import numpy as np
import  pandas as pd

num1 = [0,1,2,3,4,5,6,7,8,9]
num2 = [2,3,4,3,5,4,6,7,4,8]

x = np.array(num1)
y = np.array(num2)

from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

plt.plot(x,y , color = "r")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("first")
plt.show()