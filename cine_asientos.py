def sistema_cine():
    print("\n>>> Sistema de Asientos del Cine <<<")
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas por fila: "))
    sala = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append("L")
        sala.append(fila)
    while True:
        print("\n--- MENÚ DEL CINE ---")
        print("1) Mostrar sala")
        print("2) Reservar asiento")
        print("3) Liberar asiento")
        print("4) Contar asientos")
        print("5) Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            print("\nEstado actual de la sala:\n")
            for fila in sala:
                print(" ".join(fila))
        elif opcion == "2":
            f = int(input("Fila a reservar: ")) - 1
            c = int(input("Columna a reservar: ")) - 1

            if 0 <= f < filas and 0 <= c < columnas:
                if sala[f][c] == "L":
                    sala[f][c] = "X"
                    print("👍 Asiento reservado correctamente.")
                else:
                    print("🚫 Ese asiento ya está ocupado.")
            else:
                print("🚫 Ese asiento no existe.")
        elif opcion == "3":
            f = int(input("Fila a liberar: ")) - 1
            c = int(input("Columna a liberar: ")) - 1

            if 0 <= f < filas and 0 <= c < columnas:
                if sala[f][c] == "X":
                    sala[f][c] = "L"
                    print("👍 Asiento liberado correctamente.")
                else:
                    print("🚫 Ese asiento ya está libre.")
            else:
                print(" 🚫 Ese asiento no existe.")
        elif opcion == "4":
            libres = 0
            ocupados = 0

            for fila in sala:
                for asiento in fila:
                    if asiento == "L":
                        libres += 1
                    else:
                        ocupados += 1

            print(f"Asientos libres: {libres}")
            print(f"Asientos ocupados: {ocupados}")
        elif opcion == "5":
            print("Saliendo del sistema... Gracias.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.❎")
sistema_cine()
