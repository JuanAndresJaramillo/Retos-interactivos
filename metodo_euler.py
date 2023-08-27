
def metodo_euler( EDO, X0, N, Y0, h ):
    """
    Esta funcion resuelve EDOs de primer grado
    por medio del metodo numerico de euler
    """
    print( f"Iteracion \t X \t Y")
    y = Y0  
    x = X0
    print( "--"*15 )
    print( f"{0} \t \t {X0} \t {y}")
    for i in range( 1, N ):
        resultado = eval(EDO)
        y += h * resultado
        x += h
        print( "--"*15 )
        print( f"{i} \t \t {x} \t {y}")

resul = metodo_euler("2*x+y", 0, 5, 2, 0.2)

        
    