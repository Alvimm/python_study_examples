from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_list1 = reduce(lambda x, y: x + y, list1)

print(f'The sum of the list 1 is: {sum_list1}')

###########################################################
list2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

even_num = list(filter(lambda n: n % 2 == 0, list2))

print(f'The even numbers are: {even_num}')

##########################################################

num_list = [9.56783, 7.57568, 3.00914, 6.2321]

precision_list = [2, 2, 3, 3]

rounding = list(map(lambda x, y: round(x, y), num_list, precision_list))

print(f'The rounded numbers: {rounding}')

#########################################################

vehicles = ['airplane', 'car', 'ship', 'bus']

uppercase_name = list(map(lambda x: str.upper(x), vehicles))

print(f'The uppercase names: {uppercase_name}')
