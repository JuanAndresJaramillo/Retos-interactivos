
def metodo_euler( EDO, X0, Xf, Y0, h ):
    print( f"Iteracion \t X \t Y")
    for i in range(X0, Xf, h):
        EDO = EDO.replace("X", i)

        
    