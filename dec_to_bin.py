def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary += str(decimal % 2)
        decimal //= 2
    return binary[::-1]


decimal_base_number = eval(input('Entre com um valor na base decimal: '))
binary_base_number = decimal_to_binary(decimal_base_number)
print(f'Número na base decimal: {decimal_base_number}')
print(f'Número na base binária: {binary_base_number}')
