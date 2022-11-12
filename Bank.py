import pandas as pd
import random
import sys

# 读取BankProblem.txt
data = pd.read_table('BankProblem.txt',
                     sep=':', header=None)


# print(data)

# 适应度算法
def fitness(list):
    sum_fit, sum_weight, sum_value = 0, 0, 0
    for p in list:
        each_child_bag = p
        # print(each_child_bag)
        each_child_bag_num_split = each_child_bag.split(' ')
        each_child_bag_num = each_child_bag_num_split[1]
        # print(each_child_bag_num)
        each_child_bag_params = sum_list[int(each_child_bag_num) - 1]
        # print(each_child_bag_params)
        each_child_value = each_child_bag_params[each_child_bag]['value']
        # print(each_child_value)
        sum_value += float(each_child_value)
        # print(sum_value)
    return sum_value


# 排序算法
def dict_sorted(sort_dict):
    sorted_dict = dict(sorted(sort_dict.items(), key=lambda kv: (kv[1], kv[0])))
    return sorted_dict


key = []
for a in data[0]:
    key.append(a.strip())
value = []
for b in data[1]:
    value.append(str(b))

# print(key)
# print(value)
sum_list = []
i = 1
while i < 301:
    bag_dict = {}
    value_dict = {}
    value_dict[key[i + 1]] = value[i + 1]
    value_dict[key[i + 2]] = value[i + 2]
    bag_dict[key[i]] = value_dict
    sum_list.append(bag_dict)
    i = i + 3
# 存入sum_list
# print(sum_list)

# 创建总sum_bag_list
sum_bag_list_num = [n for n in range(1, 101)]
# print(sum_bag_list)
sum_bag_list = []
for i in sum_bag_list_num:
    a = 'bag ' + str(i)
    sum_bag_list.append(a)
# print('sum_bag_list', sum_bag_list)

# 随机取10个P传入P_data
j = 0
p_data = {}
weight_list = []
while j < 10:
    sum_cap = 0
    bag_list = []
    random_bag_list = []
    while sum_cap <= 285:
        random_bag = random.randint(0, 99)
        # print(random_weight)
        # 去除重复的取值,如果重复则重新取值
        while True:
            if random_bag in random_bag_list:
                random_bag = random.randint(0, 99)
            else:
                random_bag_list.append(random_bag)
                break
        bag_sum_list = sum_list[random_bag]
        # print(bag_weight_list)
        k = 'bag ' + str(random_bag + 1)
        # print(k)
        weight = bag_sum_list[k]["weight"]
        sum_cap = sum_cap + float(weight)
        if sum_cap <= 285:
            bag_list.append(k)
        else:
            sum_cap = sum_cap - float(weight)
            break

    p_data['p' + str(j + 1)] = bag_list
    j += 1
    # print(bag_list)
    # print(sum_cap)
    # print('p_data: ',p_data)
# print(random_weight_list)
# print(j)
h = 0
round_num = 0
while round_num < 10000:
    # print('1111111111111111')
    # TODO 获取p_data中p的数字
    p_data_p_list = []
    p_data_num_list = []
    p_data_p_list = list(p_data.keys())
    # print('p_data_p_list',p_data_p_list)
    for y in p_data_p_list:
        p_data_p_num_str = y
        p_data_p_num = int(p_data_p_num_str.strip('p'))
        # print(p_data_p_num)
        p_data_num_list.append(str(p_data_p_num))
    # print(p_data_num_list)
    # print('2222222222222222222')
    # p_data中随机得到1个parent
    def random_parent():
        random_bag = random.choice(p_data_num_list)
        # print(random_bag)
        # print(p_data_num_list)
        # print('azzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        parent_list = []
        # for l in random_bag:
        # parent_dict['p' + str(l)] = p_data['p'+str(l)]
        parent_list.append(p_data['p' + str(random_bag)])
        parent_list = parent_list[0]
        # print('parent_list: ', parent_list)
        sum_fit, sum_weight, sum_value = 0, 0, 0
        # 计算当前parent的weight and value以计算fitness
        # print(parent_list)
        # print(len(parent_list))
        for m in parent_list:
            # print('mmmmmmmmmmmmmmmmmmmmmmmmmmm')
            each_parent_split = m
            # print('eps: ', each_parent_split)
            each_bag_split_num = each_parent_split.split(' ')
            each_bag_num = each_bag_split_num[1]
            # print(each_bag_num)
            # print(sum_list)
            each_bag_params = sum_list[int(each_bag_num) - 1]
            # print("111111111")
            # print(each_bag_params)
            each_bag_weight = each_bag_params[each_parent_split]['weight']
            each_bag_value = each_bag_params[each_parent_split]['value']
            # print('777777777777777777')
            sum_weight += float(each_bag_weight)
            sum_value += float(each_bag_value)
            # print('888888888888888')
            # print(each_bag_weight,each_bag_value)
        # print('sum_weight,sum_value',sum_weight,sum_value)
        return random_bag, sum_value


    # 二元锦标赛选择parent
    def binary_tournament():

        # print('qqqqqqqqqqqqqqqqq')
        random_bag_1, sum_value_1 = random_parent()
        # print(random_bag_1, sum_value_1)
        random_bag_2, sum_value_2 = random_parent()
        # print(random_bag_2, sum_value_2)
        # print('ffffffffffffffffff')
        # print(random_bag_1)
        # print(random_bag_2)
        # print('ggggggggggggggggggggg')
        while random_bag_2 == random_bag_1:
            # print('aaaaaaaaaaaaaaaa')
            random_bag_2, sum_value_2 = random_parent()
            # print('ddddddddddddd')
            # print(random_bag_2)
            # print(random_bag_1)
            # print('jjjjjjjjjjjjjjjjj')
        if sum_value_2 >= sum_value_1:
            # print('ssssssssssss')
            parent = random_bag_2
        else:
            parent = random_bag_1
        # print(parent)
        return parent


    # 运行两次random_parent得到两个parent: 1 & 2
    parent_a = binary_tournament()
    # print('6666666666666666')
    parent_b = binary_tournament()
    '''去重，防止parent_a == parent_b'''
    # print('5555555555555555')
    while parent_b == parent_a:
        # print('99999999999999')
        parent_b = binary_tournament()
    # print('parent_a,parent_b:',parent_a,parent_b)
    # print('33333333333333333333')
    parent_a_list = p_data['p' + str(parent_a)]
    # print(parent_a_list)
    # print('列表长度：'+str(len(parent_a_list)))
    parent_b_list = p_data['p' + str(parent_b)]
    # print(parent_b_list)
    # print(len(parent_a_list),len(parent_b_list))
    # print('列表长度：'+str(len(parent_b_list)))

    # parent_a和parent_b进行crossover
    child_c = []
    child_d = []
    '''随机选取crossover部分的长度'''
    if len(parent_a_list) <= len(parent_b_list):
        part_length = random.sample(range(1, len(parent_a_list)), 1)
    else:
        part_length = random.sample(range(1, len(parent_b_list)), 1)
    print('替换长度:',part_length)
    '''随机选取crossover的起点'''
    if len(parent_a_list) <= len(parent_b_list):
        part_start = random.sample(range(0, len(parent_a_list) - int(part_length[0])), 1)
    else:
        part_start = random.sample(range(0, len(parent_b_list) - int(part_length[0])), 1)
    # print(part_start)
    '''crossover'''
    part_a = parent_a_list[int(part_start[0]):int(part_start[0]) + int(part_length[0])]
    part_b = parent_b_list[int(part_start[0]):int(part_start[0]) + int(part_length[0])]
    # print(part_a,part_b)
    del parent_a_list[int(part_start[0]):int(part_start[0]) + int(part_length[0])]
    del parent_b_list[int(part_start[0]):int(part_start[0]) + int(part_length[0])]
    for a in part_a:
        parent_b_list.insert(int(part_start[0]), a)
    for b in part_b:
        parent_a_list.insert(int(part_start[0]), b)
    # print(parent_a_list)
    # print(parent_b_list)
    '''得到child_c和child_d'''
    child_c_list = parent_a_list
    child_d_list = parent_b_list
    # print(len(child_c_list),child_c_list)
    # print(len(child_d_list),child_d_list)
    # print('44444444444444444444')
    # child_c和child_d 进行变异mutation
    '''确定变异基因的个数'''
    if len(child_c_list) <= len(child_d_list):
        mutation_max_num = len(child_c_list)
    else:
        mutation_max_num = len(child_d_list)
    mutation_num = random.sample(range(1, mutation_max_num), 1)
    # print('变异基因数量',mutation_num)
    '''从sum_bag_list中随机取mutation_num个值'''
    # print('sum_bag_list: ',sum_bag_list)
    mutation_bag_list_a = random.sample(sum_bag_list, int(mutation_num[0]))
    mutation_bag_list_b = random.sample(sum_bag_list, int(mutation_num[0]))
    # print(mutation_bag_list_a)
    # print(mutation_bag_list_b)
    '''从child_c中替换'''
    del_child_c_list = random.sample(child_c_list, int(mutation_num[0]))
    # print(del_child_c_list)
    # print(child_c_list)
    for c in del_child_c_list:
        child_c_list.remove(c)
        child_e_list = child_c_list
    # print(child_e_list)
    for e in mutation_bag_list_a:
        child_e_list.append(e)
    # print(child_e_list)
    '''从child_d中替换'''
    del_child_d_list = random.sample(child_d_list, int(mutation_num[0]))
    # print(del_child_c_list)
    # print(child_d_list)
    for d in del_child_d_list:
        child_d_list.remove(d)
        child_f_list = child_d_list
    # print(child_f_list)
    for e in mutation_bag_list_b:
        child_f_list.append(e)
    # print(child_f_list)

    # child_e & child_d去重
    child_e_list = list(set(child_e_list))
    child_f_list = list(set(child_f_list))
    # print(len(child_e_list),child_e_list)
    # print(len(child_f_list),child_f_list)

    # 评估e和f的适应度
    child_e_value = fitness(child_e_list)
    child_f_value = fitness(child_f_list)
    # print(child_e_value,child_f_value)

    # 评估p_data中每一个P的适应度
    # print(p_data)
    p_sum_value_list = []
    for q in p_data:
        each_p_sum_value = 0
        each_p_data_list = p_data[q]
        # print(each_p_data_list)
        for p in each_p_data_list:
            each_p_data_split = p
            # print(each_p_data_split)
            each_p_data_split_num = each_p_data_split.split(' ')
            each_p_data_num = each_p_data_split_num[1]
            # print(each_p_data_num)
            each_p_data_params = sum_list[int(each_p_data_num) - 1]
            # print(each_p_data_params)
            each_p_data_value = each_p_data_params[each_p_data_split]['value']
            # print(each_p_data_value)
            each_p_sum_value += float(each_p_data_value)
        # print(each_p_sum_value)
        p_sum_value_list.append(each_p_sum_value)
    # print(p_sum_value_list)
    # 将每个P的总value与P对应

    # '''创建p1~p10的list'''
    # p_value_p_num = [n for n in range(1, 11)]
    # # print(p_value_p_num)
    # p_value_p = []
    # for x in p_value_p_num:
    #     p_num = 'p' + str(x)
    #     p_value_p.append(p_num)
    # print(p_value_p)

    '''p_data_p_list 与 p_value_p对应创建dict'''
    p_value = dict(zip(p_data_p_list, p_sum_value_list))
    # print('p_value',p_value)

    # 对p_value排序
    p_value_sorted = dict_sorted(p_value)
    # print(p_value_sorted)

    # 得到最小的value
    for key, value in p_value_sorted.items():
        p_min_value_sorted = (value)
        p_min_key_sorted = (key)
        break
    # print(p_min_key_sorted,p_min_value_sorted)
    # 与child_e_value对比大小
    # print(child_e_value,child_f_value)
    if float(child_e_value) >= float(p_min_value_sorted):
        h += 1
        del p_value_sorted[p_min_key_sorted]
        p_value_sorted['p' + str(j + h)] = child_e_value
        p_value_e = p_value_sorted
        # 并删除p_data中的数据
        del p_data[p_min_key_sorted]
        # 将child_e加入p_data
        p_data['p' + str(j + h)] = child_e_list
        # print(p_value_sorted)
        # print(p_data)
        # print('p_value_e')
        # print(p_value_e)
        # 对p_value_e排序
        p_value_e_sorted = dict_sorted(p_value_e)
        final_value = p_value_e_sorted
        # print('p_value_e_sorted:',p_value_e_sorted)
        # 再次得到最小值，并于child_f_value对比大小
        for key, value in p_value_e_sorted.items():
            p_min_value_e_sorted = (value)
            p_min_key_e_sorted = (key)
            break
        if float(child_f_value) >= float(p_min_value_e_sorted):
            h += 1
            del p_value_e_sorted[p_min_key_e_sorted]
            p_value_e_sorted['p' + str(j + h)] = child_f_value
            p_value_e_f = p_value_e_sorted
            # 并删除p_data中的数据
            del p_data[p_min_key_e_sorted]
            # 将child_f加入p_data
            p_data['p' + str(j + h)] = child_f_list
            # print(p_data)
            # print('p_value_e_f')
            # print(p_value_e_f)
            # 对p_value_e排序
            p_value_e_f_sorted = dict_sorted(p_value_e_f)
            final_value = p_value_e_f_sorted
            # print('p_value_e_f_sorted:',p_value_e_f_sorted)
    else:
        if float(child_f_value) >= float(p_min_value_sorted):
            h += 1
            del p_value_sorted[p_min_key_sorted]
            p_value_sorted['p' + str(j + h)] = child_f_value
            p_value_f = p_value_sorted
            # 并删除p_data中的数据
            del p_data[p_min_key_sorted]
            # 将child_f加入p_data
            p_data['p' + str(j + h)] = child_f_list
            # print(p_data)
            # print('p_value_f')
            # print(p_value_f)
            # 对p_value_e排序
            p_value_f_sorted = dict_sorted(p_value_f)
            final_value = p_value_f_sorted
            # print('p_value_f_sorted:',p_value_f_sorted)
    round_num += 1
    print('round_num = ' + str(round_num))
    print(final_value)
