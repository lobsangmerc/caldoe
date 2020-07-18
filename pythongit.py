import os 
dolar = float(58.5)
euro = float(66.8)




def operaciones_dolar():
    print('1.DOLAR A PESO              2.PESO A DOLAR')
    dolar_op = int(input("Ingrese la operacion que desea realizar: "))
    if dolar_op == 1:
        print('Esta convirtiendo de dolar a peso dominicano')
        cantidad = int(input('Ingrese la cantidad que desea convertir: '))
        total = float(cantidad*dolar)
        print('sus dolares son: {} pesos dominicanos '.format(total) )
        print('Desea volver al inicio?')
        print ('1.SI         2.NO')
        opcion2= int(input('Ingrese la opcion deseada: '))
        if opcion2 == 1:
            os.system("cls")
            run()
        elif opcion2 ==2:
            exit()
    elif dolar_op ==2:
        print('Esta convirtiendo de peso dominicano a dolar')
        cantidad = int(input('Ingrese la cantidad que desea convertir: '))
        total = float(cantidad/dolar)
        print('sus pesos son: {} dolares '.format(total) )
        print('Desea volver al inicio?')
        print ('1.SI         2.NO')
        opcion2= int(input('Ingrese la opcion deseada: '))
        if opcion2 == 1:
            os.system("cls")
            run()
        elif opcion2 ==2:
            exit()
        
        

def operaciones_euro():
    print('1.EURO A PESO              2.PESO A EURO')
    dolar_op = int(input("Ingrese la operacion que desea realizar: "))
    if dolar_op == 1:
        print('Esta convirtiendo de euro a peso dominicano')
        cantidad = int(input('Ingrese la cantidad que desea convertir: '))
        total = float(cantidad*euro)
        print('sus euros son: {} pesos dominicanos '.format(total) )
        print('Desea volver al inicio?')
        print ('1.SI         2.NO')
        opcion2= int(input('Ingrese la opcion deseada: '))
        if opcion2 == 1:
            os.system("cls")
            run()
        elif opcion2 ==2:
            exit()
    elif dolar_op ==2:
        print('Esta convirtiendo de peso dominicano a euros')
        cantidad = int(input('Ingrese la cantidad que desea convertir: '))
        total = float(cantidad/euro)
        print('sus pesos son: {} euros '.format(total) )
        print('Desea volver al inicio?')
        print ('1.SI         2.NO')
        opcion2= int(input('Ingrese la opcion deseada: '))
        if opcion2 == 1:
            os.system("cls")
            run()
        elif opcion2 ==2:
            exit()







def run():
    print("Esta es una calculadora para divisas")
    print("1.Operaciones con dolares")
    print("2.Operaciones con Euros")
    opcion = int(input("Ingresa la opcion: "))
    if opcion == 1:
        operaciones_dolar()
    elif opcion == 2:
        operaciones_euro()
    elif opcion == 3:
        os.system("cls")
        run()
    






if __name__ == "__main__":
    run()