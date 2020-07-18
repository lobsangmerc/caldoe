
def run():
    print("Esta es una calculadora para divisas")
    print("1.Peso Dominicano a dolar")
    print("2.Peso Dominicano a euro")
    print("3.Dolar a peso dominicano")
    print("4.Euro a peso dominicano")
    opcion = int(input("Ingresa la opcion: "))
    if opcion == 1:
        peso_a_dolar()
    elif opcion == 2:
        peso_a_euro()
    elif opcion == 3:
        dolar_a_peso()
    elif opcion == 4:
        euro_a_peso()

    






if __name__ == "__main__":
    run()