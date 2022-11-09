import pandas as pd
import random
from random import sample

# 读取BankProblem.txt
data = pd.read_table('BankProblem.txt',
                     sep=':', header=None,
                     skiprows=1)
print(type(data))
key = []
for a in data[0]:
    key.append(a.strip())
value = []
for b in data[1]:
    value.append(str(b))
bag_dict = {}
print(key)
print(value)
sum_list = []
i = 1
while i < 301:
    value_dict = {}
    value_dict[key[i+1]] = value[i+1]
    value_dict[key[i+2]] = value[i+2]
    bag_dict[key[i]] = value_dict
    sum_list.append(bag_dict)
    i = i+3
print(value_dict)

