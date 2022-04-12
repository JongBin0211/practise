#다변량
import pandas as pd

fish_multi = pd.read_csv("./data/3-2-1-fish_multi.csv")
print(type(fish_multi))
print(fish_multi)
print(fish_multi.groupby("species"))
print("--------------------")




shoes = pd.read_csv("./data/3-2-2-shoes.csv")
print(type(shoes))
cross = pd.pivot_table(
    data = shoes,
    values = "sales",
    aggfunc = "sum",
    columns = "color"
)
print(cross)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

store_cross = pd.pivot_table(
    data = shoes,
    values = "sales",
    aggfunc = "sum",
    columns = "store"
)
print(store_cross)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

store_cross1 = pd.pivot_table(
    data = shoes,
    values = "sales",
    aggfunc = "sum",
    columns = "store",
    index = "store"
)
print(store_cross1)
