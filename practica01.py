import time
def mostrar_menu():


    print("\nMenú:")
    print("1. Metodo por Ordenamiento de Burbuja")
    print("2. Metodo por Ordenamiento de Burbuja Optimizada")
    print("3. Byeeeeee....")

def ord_burbuja(arr):
    n = len(arr)

    for i in range(n-1):       
        for j in range(n-1-i): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def burbuja_optimizada(arr):
    n = len(arr)
    for i in range(n-1):
        intercambio = False

        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambio = True

        if  intercambio == False:
            break

def ingresar_lista():
    try:
        n = int(input("Ingrese el tamaño de su lista: "))
        lista = []
        for i in range(n):
            elemento = int(input("Ingrese el elemento por cada elemento: "))
            lista.append(elemento)
        return lista
    except ValueError:
        print("Numero invalido, por favor, ingrese otro.")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción que desea ejecutar: ")


    if opcion == "1":
        inicio = time.time()

        lista = ingresar_lista()
        if lista:
            ord_burbuja(lista)
            print("\nLista ordenada con el Metodo Burbuja:")
            print(lista)

            fin = time.time()
        tiempo_ejecutado = fin-inicio
        print(tiempo_ejecutado)


    elif opcion == "2":
        inicio = time.time()

        lista = ingresar_lista()
        if lista:
            burbuja_optimizada(lista)
            print("\nLista ordenada con el Metodo Burbuja Optimizado:")
            print(lista)

            fin = time.time()
        tiempo_ejecutado = fin-inicio
        print(tiempo_ejecutado)


    elif opcion == "3":
        print("Saliendo del programa. Y puros corridos tumbados, Eaaaaaaaa...!!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido del menú.")