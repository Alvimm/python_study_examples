def collect_data():
    data_list = []
    data_index = 0
    data_set = eval(input('Define the set size: '))

    while len(data_list) < data_set:
        data_list.append(input(f'Enter list element number {data_index + 1}: '))
        data_index += 1

    return data_list


def intermediate_calculations(data_list):
    aux_list = []
    combinations = [[]]

    for i in data_list:
        aux_list.append(i)
        combinations.append([i])

    for x in data_list:
        for y in aux_list:
            if aux_list.index(y) >= data_list.index(x) + 1:
                combinations.append([x, y])

    combinations.append(data_list)

    return combinations


def presenting_data():
    combinations = intermediate_calculations(collect_data())

    print(f'These are the sets of the part of the set: {combinations}')


presenting_data()
