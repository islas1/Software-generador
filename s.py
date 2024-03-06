def congruencial_aditivo():
    # Solicitar al usuario que ingrese el número de semillas, el valor de m y el valor de N
    num_semillas = int(input("Ingrese el número de semillas: "))
    m = int(input("Ingrese el valor de m: "))
    N = int(input("Ingrese el valor de N: "))

    # Solicitar al usuario que ingrese las semillas
    semillas = []
    for i in range(num_semillas):
        semilla = int(input(f"Ingrese la semilla {i + 1}: "))
        semillas.append(semilla)

    # Crear la lista x con las semillas
    x = semillas.copy()

    # Calcular la secuencia x usando la ecuación recursiva
    for i in range(num_semillas + 1, N + 1):
        xi = (x[i - 2] + x[i - num_semillas - 1]) % m
        x.append(xi)

    # Calcular la secuencia de números pseudoaleatorios r
    for i, xim in enumerate(x[num_semillas:], start=num_semillas + 1):
        ri = xim / (m - 1)
        print(f"x{i}: {xim}, ri: {ri}")  # Formateamos ri con 4 decimales

def congruencial_multiplicativo():
   
    while True:
        try:
            a = int(input("Ingrese el multiplicador (a): "))
            m = int(input("Ingrese el módulo (m): "))
            semilla = int(input("Ingrese la semilla inicial (semilla): "))
            n = int(input("Ingrese el número de valores a generar (n): "))
            break  # Si todos los valores son enteros, salimos del bucle
        except ValueError:
            print("Por favor, ingrese valores enteros válidos.")

    xn = semilla
    x_values = []
    r_values = []
    for _ in range(n):
        xn = (a * xn) % m
        ri = xn / (m - 1)
        x_values.append(xn)
        r_values.append(ri)
    for x, r in zip(x_values, r_values):
        print(f"Xn: {x}, Ri: {r}")

def MultiplicadorConstante():
    semilla = int (input("Ingresa el rango de la semilla: "))
    xi = int (input("Ingresa el valor de la semilla: "))
    const = int (input("Ingrese el valor de la constante: "))

    def centro(size, number):
        s = str(number)
        li = (len(s) - size) // 2
        ls = li + size
        return s[li:ls]

    ri = []
    for i in range(semilla):
        xi = const * xi
        c = centro(len(str(xi)), xi)
        xi = int(c)
        ri.append(float("0." + c))
    print(ri)

def Congruencial_Mixto():
    ri = []
    xi = int(input("Dame el valor de la semilla: "))
    a = int(input("Dame el valor de la constante multiplicativa: "))
    c = int(input("Dame el valor de la constante aditiva: "))
    m = int(input("Dame el valor del modulo: "))
    cantidad = int(input("Cantidad de periodo: "))

    for i in range(cantidad):
        xi = (a * xi + c) % m
        ri.append(xi/m)
    print(ri)
    return ri

def productosMedios():
    
    band=True
    
    while band: 
      try:
        semillaUno = int (input("Ingrese el valor de la semilla uno: "))
        semillaDos = int (input("Ingrese el valor de la semilla uno: "))
      except ValueError:
        print ("Ingrese valores enteros validos")
        
      if semillaUno<3 or semillaDos<3:
          print("Valores menores a tres digitos, vuelva a intentar")       
      else:
          band=False
    
    while True:
      try: 
        valoresGen= int (input ("Ingresa la cantidad de valores a generar: "))
        break
      except ValueError:
          print ("Ingrese valores enteros validos")
          
    auxUno=str(semillaUno)
    auxDos=str(semillaDos)
          
    if len(auxUno)>len(auxDos):
        auxcadena=len(auxUno)
    elif len(auxDos)>len(auxUno):
        auxcadena=len(auxDos)
    elif len(auxDos) == len(auxUno):
        auxcadena=len(auxUno)
          
    
    multi=semillaUno*semillaDos
    longCadena= len(str(multi))
    strmulti=str(multi)
    
    for i in range (0, valoresGen):
        multi=semillaUno*semillaDos
        longCadena= len(str(multi))
        strmulti=str(multi)
        if auxcadena%2==0:
            if longCadena%2 ==0:
                valaTomar=(longCadena-auxcadena)/2
                newCadena=strmulti[int(valaTomar): int(longCadena)-int(valaTomar)]
                print ("Y",i," = (",semillaUno," + ",semillaDos,") = ",multi,"  x",i+1," = ",newCadena," r",i+1," = ",(int(newCadena))*10**(-1*len(newCadena)))
                semillaUno=semillaDos
                semillaDos=int(newCadena)
            elif longCadena%2 != 0:
                valaTomar=(longCadena-auxcadena+1)/2
                newCadena=strmulti[int(valaTomar)-1: int(longCadena)-int(valaTomar)]
                print ("Y",i," = (",semillaUno," + ",semillaDos,") = ",multi,"  x",i+1," = ",newCadena," r",i+1," = ",(int(newCadena))*10**(-1*len(newCadena)))
                semillaUno=semillaDos
                semillaDos=int(newCadena)
        elif auxcadena%2 != 0: 
            if longCadena%2 ==0:
                valaTomar=(longCadena-auxcadena+1)/2
                newCadena=strmulti[int(valaTomar)-1: int(longCadena)-int(valaTomar)]
                print ("Y",i," = (",semillaUno," + ",semillaDos,") = ",multi,"  x",i+1," = ",newCadena," r",i+1," = ",(int(newCadena))*10**(-1*len(newCadena)))
                semillaUno=semillaDos
                semillaDos=int(newCadena)
            if longCadena%2 != 0:
                valaTomar=(longCadena-auxcadena)/2
                newCadena=strmulti[int(valaTomar): int(longCadena)-int(valaTomar)]
                print ("Y",i," = (",semillaUno," + ",semillaDos,") = ",multi,"  x",i+1," = ",newCadena," r",i+1," = ",(int(newCadena))*10**(-1*len(newCadena)))
                semillaUno=semillaDos
                semillaDos=int(newCadena)
                
def cuadrados_medios(sem, digitos, Rs):
    resultados = []
    for _ in range(Rs):
        cuadrado = sem ** 2
        cuadrado_str = str(cuadrado)
        longitud_total = len(cuadrado_str)
        mitad = longitud_total // 2
        inicio = mitad - digitos // 2
        final = mitad + digitos // 2
        nueva_semilla = int(cuadrado_str[inicio:final])
        if nueva_semilla >= 10**digitos:
            nueva_semilla = nueva_semilla // 10
        resultados.append(nueva_semilla / (10 ** digitos))
        sem = nueva_semilla
    return resultados
       
      
# Menú de selección
while True:
    print("1. Congruencial Aditivo")
    print("2. Congruencial Multiplicativo")
    print("3. Congruencial Mixto")
    print("4. Cuadrados Medios")
    print("5. Productos Medios")
    print("6. Multiplicativo constante")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        congruencial_aditivo()
    elif opcion == "2":
        congruencial_multiplicativo()
    elif opcion == "3":
        Congruencial_Mixto()
    elif opcion == "4":
        Sem = input("Ingrese la semilla: -----> ")
        resultado = Sem.isnumeric()
        if resultado == True :
          Semi = int(Sem)
          sem = Semi
          tam = len(Sem)
          tamint = int(tam)
          digitos = tamint
          Rs = 20
          resultados = cuadrados_medios(sem, digitos, Rs)
          print("")
        for i, num in enumerate(resultados, start=1):
             print(f"R{i}: {num}")
    elif resultado == False :
        print("Ingrese datos numericos")
    elif opcion == "5":
        congruencial_multiplicativo()
    elif opcion == "6":
        congruencial_multiplicativo()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
