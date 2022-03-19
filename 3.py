# Punto 3

def Product(cod, name, price):
    return {
        "cod": cod,
        "name": name,
        "price": price,
    }


condition = 10
products = [{"cod": "1", "name": "name1", "price": "price1"}]
print(f'{products}')

while(condition != 0):
    print(".......Menú........")
    print("Digitar 1 para recibir {código, nombre, precio} de un producto")
    print("Digitar 2 para mostrar todos los productos registrados")
    print("Digitar 3 para permitir buscar por código un producto y editar el precio de este")
    print(
        "Digitar 4 para permitir buscar por código un producto y eliminar el producto")
    print("Digitar 0 para SALIR")
    print("....................")
    condition = int(input())
    if(condition == 1):
        print("Digita codigo del producto")
        cod = input()

        print("Digita nombre del producto")
        name = input()

        print("Digita precio del producto")
        price = input()

        pr = Product(cod, name, price)
        products.append(pr)
    if(condition == 2):
        print(f'{products}')
    if(condition == 3):
        print("ingresa el codigo del producto que deseas buscar")
        cod = input()
        for p in products:
            if p["cod"] == cod:
                newPrice = int(input("Digite el nuevo precio:  "))
                p["price"] = newPrice
                print(products)
            else:
                print("Este producto no existe")
    if condition == 4:
        print("ingresa el codigo del producto que deseas eliminar")
        cod = input()
        for p in products:
            if p["cod"] == cod:
                products.remove(p)
                print(f'Producto eliminado')
            else:
                print("Este producto no existe")
    if condition < 0 and condition > 4:
        print("Digita una opción valida")
