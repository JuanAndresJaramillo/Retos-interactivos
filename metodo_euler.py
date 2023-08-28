
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
    caracteres_malos = 0
    while bandera == 0:
        ecuacion = input(mensaje) 
        for char in ecuacion:
            if caracteres_permitidos.count(char) == 0:
                print( f"El caracter {char} no puede ser incluido en la ecuacion" )
                caracteres_malos +=1
        if caracteres_malos == 0:
            break
        else:
            print( f"Usted tiene {caracteres_malos} caracter(es) malos.", 
                  "vuelva a ingresar la ecuacion de manera correcta")
    return ecuacion


    