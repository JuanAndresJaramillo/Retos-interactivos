
def metodo_euler( EDO, X0, Y0, N, h ):
    """
    Esta funcion resuelve EDOs de primer grado
    por medio del metodo numerico de euler
    """
    print( f"Iteracion \t X \t Y")
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

resul = metodo_euler("(x**2-1)/y**2", 0, 2, 5, 0.2)

        
    