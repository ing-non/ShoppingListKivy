import math

buy = {}
stock = {"Eier" : 0, "Mehl" : 50}
pancake = {"Mehl" : 156, "Eier": 0.5}
pala = {"Mehl" : 200, "Eier" : 2}
menu = [pancake, pala]

for i in menu:
    for k in i.keys():
        buy.setdefault(k, 0)
        buy[k] = buy[k] + i[k]

for k in buy.keys():
    buy[k] = buy[k] - stock[k]
    if buy[k] < 0:
        buy[k] = 0
    buy[k] = math.ceil(buy[k])
print(buy)