import pandas as pd
import random

# 读取BankProblem.txt
data = pd.read_table('BankProblem.txt',
                     sep=':', header=None)
# print(type(data))
key = []
for a in data[0]:
    key.append(a.strip())
value = []
for b in data[1]:
    value.append(str(b))
bag_dict = {}
# print(key)
# print(value)
sum_list = []
i = 1
while i < 301:
    value_dict = {}
    value_dict[key[i + 1]] = value[i + 1]
    value_dict[key[i + 2]] = value[i + 2]
    bag_dict[key[i]] = value_dict
    sum_list.append(bag_dict)
    i = i + 3
# 存入sum_list
# print(sum_list)

# 随机取P
j = 0
p_data = {}
sum_cap = 0
bag_list = []
weight_list = []
random_weight_list = []
while j < 10:
    while sum_cap < 285:
        random_weight = random.randint(0, 99)
        # print(random_weight)
        # 去除重复的取值,如果重复则重新取值
        if random_weight in random_weight_list:
            random_weight = random.randint(0, 99)
        else:
            random_weight_list.append(random_weight)

        bag_weight_list = sum_list[random_weight]
        # print(bag_weight_list)

        k = 'bag ' + str(random_weight + 1)
        print(k)

        weight = bag_weight_list[k]["weight"]
        sum_cap = sum_cap + float(weight)
        if sum_cap < 285:
            bag_list.append(k)
        else:
            sum_cap = sum_cap - float(weight)
            break

    p_data['p' + str(j + 1)] = bag_list
    j += 1
    print(bag_list)
    # print(sum_cap)
    # print(p_data)
    # print(random_weight_list)
    print(j)
