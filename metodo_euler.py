
def metodo_euler( EDO, X0, Y0, N, h ):
    """
    Esta funcion resuelve EDOs de primer grado
    por medio del metodo numerico de euler
    """
    print( f"\nIteracion \t X \t Y")
    y = Y0  
    x = X0
    print( "--"*15 )
    print( f"{0} \t \t {X0} \t {y}")
    for i in range( 1, N+1 ):
        resultado = eval(EDO)
        y += h * resultado
        x += h
        print( "--"*15 )
        print( f"{i} \t \t {round(x,4)} \t {round(y,4)}")
    print("\n")


def ingresar_numero_entero_positivo(mensaje):
    bandera = 0
    while (bandera == 0):
        numero = int(input(mensaje))
        if numero > 0:
            bandera = 1
        else:
            print( "Digite un numero entero positivo\n")
    return numero

def ingresar_numero_real_positivo(mensaje):
    bandera = 0
    while (bandera == 0):
        numero = float(input(mensaje))
        if numero > 0:
            bandera = 1
        else:
            print( "Digite un numero real positivo\n")
    return numero
    
def ingresar_ecuacion(mensaje, caracteres_permitidos):
    bandera = 0
    while bandera == 0:
        ecuacion = input(mensaje)
        caracteres_malos = 0 
        for char in ecuacion:
            if caracteres_permitidos.count(char) == 0:
                print( f"El caracter {char} no puede ser incluido en la ecuacion" )
                caracteres_malos +=1
        if caracteres_malos == 0:
            break
        else:
            print( f"Usted tiene {caracteres_malos} caracter(es) malo(s).", 
                  "vuelva a ingresar la ecuacion de manera correcta")
    return ecuacion


x_inicial = float(input("Digite cuanto vale x en sus condiciones iniciales (X0): "))
y_inicial = float(input("Digite cuanto vale Y en sus condiciones iniciales (Y0): "))
numero_de_pasos = ingresar_numero_entero_positivo("Digite su numero de pasos: ")
paso = ingresar_numero_real_positivo("Digite el paso de su ejercicio: ")
ecuacion_diferencial = ingresar_ecuacion("Digite su ecuacion diferencial despejada en terminos de dy/dx \n solo se admiten las variables \"x\" y \"y\": ", "0123456789+-*/()xy")
resultado = metodo_euler(ecuacion_diferencial, x_inicial, y_inicial, numero_de_pasos, paso)


