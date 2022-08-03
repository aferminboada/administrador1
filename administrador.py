def inicio():
    excel_edificio = {
        "nombre_edificio" : "",
        "cantidad_pisos": 0,
        "cantidad_apartamentos_por_piso": 0,
        "cantidad_apartamentos_totales":0,
        "gastos_mes": {
            "5":0,
            "6":0,
            "7":0,
        },
        "gastos_totales_edificio":0,
    }
    menu = 0
    while menu < 13:
        menu = int(input("Hola administrador\n"
                         "Deseas cargar el nombre del edificio, marca 1, \n "
                         "Deseas cargar la cantidad de pisos del edificio y apartamentos, marca 2, \n"
                         "Deseas cargar los gastos, marca 3,\n"
                         "Deseas observar los gastos cargados, marcar 4 \n"
                         "Deseas ver las expensas por aparamento por mes, marca 5 \n"
                         "Deseas saber la cantidad de apartamentos que hay en el edficio, marca 6 \n"
                         "Deseas saber la deuda por apartamento, marca 7"
                         "Deseas salir del programa, marca 8\n"
                         "elija una opcion: "))
        if menu == 1:
            edificio = crear_edificio()
            excel_edificio["nombre_edificio"] = edificio
        elif menu == 2:

            cant_pisos, cant_apartamento, total_apartamentos = apartamentos(edificio)
            excel_edificio["cantidad_pisos"] = cant_pisos
            excel_edificio["cantidad_apartamentos_por_piso"] = cant_apartamento
            excel_edificio["cantidad_apartamentos_totales"] = total_apartamentos
            print(excel_edificio)

        elif menu == 3:
            total_gasto, mes_gasto, detalle_mes = gastos()
            excel_edificio["gastos_mes"][str(mes_gasto)] = total_gasto
            print(excel_edificio)
        elif menu == 5:
            pass
        elif menu == 6:
            total_ap = excel_edificio["cantidad_apartamentos_totales"]
            print("La cantidad tatal de apartamentos es de " + str(total_ap))
        else:
            exit()

def crear_edificio():

    edificio = (input("Cual es el nombre del edificio?: "))
    return edificio

def apartamentos(edificio):
    print(edificio, type(edificio))
    cant_pisos = int(input("Cuantos pisos hay en el edificio: "))
    cant_apartamento = int(input("Cuantos apartamentos hay por piso: "))
    total_apartamentos = cant_pisos * cant_apartamento
    print("En el edificio hay " + str(total_apartamentos) + " apartamentos en total")
    return cant_pisos, cant_apartamento, total_apartamentos

#apartamentos("lui")

def gastos():
    mes_gasto = int(input("Elige de que mes deseas acargar el gasto:\n "
                          "presiona 1, para enero\n"
                          "presiona 2, para febrero\n"
                          "presiona 3, para marzo\n"
                          "presiona 4, para abril\n"
                          "presiona 5, para mayo\n"
                          "presiona 6, para junio\n"
                          "presiona 7, para julio\n"
                          "presiona 8, para agosto\n"
                          "preisona 9, para septiembre\n"
                          "presiona 10, para octubre\n"
                          "presiona 11, para noviembre\n"
                          "presiona 12, para diciembre\n"
                          "selecciona una opcion: "))
    if mes_gasto >= 1 and mes_gasto <= 12:
        mes = []
        cant_gastos = int(input("Cuantos gastos deseas cargar, escribe en numeros: "))
        total_gasto = 0
        for i in range(0, cant_gastos):
                nombre_gasto = input("Introduce el nombre del gasto: ")
                monto_gasto = float(input("Introduce el monto del gasto: "))
                total_gasto = total_gasto + monto_gasto
                print("EL total de los gastos son: " + str(total_gasto) + " " + "del mes " + str(mes_gasto ))
                mes.append(monto_gasto)
        print(mes)
        return total_gasto, mes_gasto, mes

    else:
        exit()


inicio()

def deuda():
    pass


