

print("Presiona Ctrl+C para salir...\n")

try:
    while True:
        edad = None
        while edad == None:
            try:
                edad = int(input("Ingresa tu edad: "))
            except ValueError:
                print("[Error] Ingrese una edad valida\n")

        print("")
        if edad >= 18:
            print("Eres legal en México")
        else:
            print("No eres legal en México")
except KeyboardInterrupt:
    print("\nTerminando el programa...")