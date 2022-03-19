# Punto 1
import numbers
number = int(input("¿Cuantos numeros desea ingresar? "))
numbers = []
multiples = []
multiples2 = []
multiples3 = []

for i in range(number):
    print(f'Ingresa numero #{i+1}')
    n = int(input())
    numbers.append(n)
    if(n % 2 == 0 and n % 3 == 0):
        multiples.append(n)
    if(n % 2 == 0):
        multiples2.append(n)
    if(n % 3 == 0):
        multiples3.append(n)
print(f'Numeros ingresados')
print(f'{numbers}')
print(f'Total {len(numbers)}')
print("..........")
print(f'Multiplos de 2')
print(f'{multiples2}')
print(f'Total {len(multiples2)}')
print("..........")
print(f'Multiplos de 3')
print(f'{multiples3}')
print(f'Total {len(multiples3)}')
print("..........")
print(f'Multiplos de 2 y 3')
print(f'{multiples}')
print(f'Total {len(multiples)}')
print("..........")
