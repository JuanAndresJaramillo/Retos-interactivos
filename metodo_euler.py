
def metodo_euler( EDO, X0, Xf, Y0, h ):
    print( f"Iteracion \t X \t Y")
    y = Y0
    i = 0
    print( "--"*6 )
    print( f"{i} \t \t {X0} \t {y}")
    for x in range(X0, Xf, h):
        resultado = eval(EDO)
        y += h * resultado
        i += 1
        print( "--"*6 )
        print( f"{i} \t {x} \t {y}")

resul = metodo_euler("2*x+y", 0, 1, 2, 0.2)

        
    