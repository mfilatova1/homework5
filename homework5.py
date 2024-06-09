immutable_var = 1,2,3,"hello", True
immutable_var_1 = (1,2,3,"hello", True)
immutable_var_2 = tuple ([1,2,3,"hello", True])
print(immutable_var)
print(immutable_var_1)
print(immutable_var_2)
# print(mutable_list)#immutable_var[0] = 11
# print(immutable_var) значения элементов кортежа являются неизменяемыми, так как основная функция кортежа, в отличие от списка, оставить данные внутри списка неизменными
mutable_list = ["ручка", "карандаш", "выделитель", "наушники"]
print(mutable_list)
mutable_list [0] = "линейка"
mutable_list [-1] = "тетрадь"
print(mutable_list)

