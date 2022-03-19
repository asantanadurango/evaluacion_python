# Punto 2
print(f'Ingresa 10 frutas')
fruits = []

count = 1
for i in range(10, 0, -1):
    print(f'Ingresa fruta #{count}')
    f = input()
    fruits.append(f)
    count += 1
fruits.reverse()
print(f'{fruits}')
