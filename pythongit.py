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
        total = float(dolar*cantidad)
        print('sus dolares son: {} pesos dominicanos '.format(total) )
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
    print("1.Peso Dominicano a dolar")
    print("2.Peso Dominicano a euro")
    print("3.Dolar a peso dominicano")
    print("4.Euro a peso dominicano")
    opcion = int(input("Ingresa la opcion: "))
    if opcion == 1:
        operaciones_dolar()

    #elif opcion == 2:
        #peso_a_euro()
   # elif opcion == 3:
        #dolar_a_peso()
    #elif opcion == 4:
        #euro_a_peso()

    






if __name__ == "__main__":
    run()