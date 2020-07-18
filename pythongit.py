
dolar = float(58.56)
euro = float(66.86)




def peso_a_dolar():
    cantidad = int(input('Ingrese la cantidad que desea convertir: '))
    total = float(cantidad*dolar)
    print(total)
    print('Desea volver al inicio?')
    print ('1.SI         2.NO')
    opcion2= int(input('Ingrese la opcion deseada: '))
    if opcion2 == 1:
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
        peso_a_dolar()

    #elif opcion == 2:
        #peso_a_euro()
   # elif opcion == 3:
        #dolar_a_peso()
    #elif opcion == 4:
        #euro_a_peso()

    






if __name__ == "__main__":
    run()