import math
import my_lib

a = eval(input('Entre com o coeficiente a da equação: '))
b = eval(input('Entre com o coeficiente b da equação: '))
c = eval(input('Entre com o coeficiente c da equação: '))

delta = my_lib.calculate_delta(a, b, c)

print(f'O valor calculado do delta foi {delta}')

if delta > 0:
    print('A equação tem DUAS raízes reais.')
    root_1 = (-b + math.sqrt(delta)) / 2 * a
    root_2 = (-b - math.sqrt(delta)) / 2 * a
    print(f'As raízes da equação são {root_1} e {root_2}')
elif delta == 0:
    print('A equação tem UMA raiz real.')
    root = (-b + math.sqrt(delta)) / 2 * a
    print(f'A raiz da equação é {root}')
else:
    print('A equação NÃO tem raiz real.')

