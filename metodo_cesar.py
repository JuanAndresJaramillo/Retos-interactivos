def ingresar_numero_entero_positivo(mensaje): #Funcion para ingresar numero positivo entero
    bandera = 0
    while (bandera == 0):
        numero = input(mensaje)
        if numero.isdigit() == True: #Verificar que si sea un digito el numero ingresado
            numero = int(numero)
            if numero > 0:
                bandera = 1
            else:
               print( "Digite un numero entero positivo\n") 
        else:
            print( "Digite un numero entero positivo\n")
    return numero

def ingresar_opcion(mensaje, opciones, numero_letras_respuesta): #Funcion para pedir opcion
    bandera = 0
    while bandera == 0:
        opcion_escogida = input(mensaje)
        caracteres_malos = 0 
        for char in opcion_escogida:
            if opciones.count(char) == 0: #Verificar si el caracter esta en las opciones
                print( f"El caracter {char} no puede ser seleccionado" ) #Sino esta el caracter imprime
                caracteres_malos +=1
            elif len(opcion_escogida) != numero_letras_respuesta: #Controla que la opcion no tenga mas letras de las permitidas
                caracteres_malos += 1
        if caracteres_malos == 0:
            break
        else:
            print( f"Ingrese una opcion valida") #Si hay caracteres malos pide que ingrese una opcion valida
    return opcion_escogida

def codificar(mensaje, desplazamiento):
    print( f" \nel mensaje \"{mensaje}\" codificado es: " )
    for char in mensaje:
        if char != ' ':   #Para que no codifique los espacios
            numero_caracter = ord(char) #Obtener el valor del caracter
            numero_codificado = numero_caracter + (desplazamiento % 26)
            if numero_codificado > 122 or (numero_codificado > 90 and numero_codificado < 97):
                numero_codificado -= 26     #ya que las ultimas letras del abecedario se codifican desplazandose al inicio
            print( f"{chr(numero_codificado)}", end="" )
        else:
            print( f" ", end='' )
    print("\n")

def decodificar(mensaje_codificado, desplazamiento):
    print( f" \nel mensaje \"{mensaje_codificado}\" decodificado es: " )
    for char in mensaje_codificado:
        if char != ' ':
            numero_caracter = ord(char) 
            numero_decodificado = numero_caracter - (desplazamiento % 26)
            if numero_decodificado < 65 or (numero_decodificado > 90 and numero_decodificado < 97):
                numero_decodificado += 26  #Ya que las primeras letras del abecedario decodifican desplazandose al final
            print( f"{chr(numero_decodificado)}", end="" )
        else:
            print( f" ", end='' )
    print("\n")

def ingresar_alpha(mensaje):
    palabras_incorrectas = 1
    while palabras_incorrectas != 0:
        string = input(mensaje)
        string = string.split()  #para que acepte el mensaje con espacios 
        palabras_incorrectas = 0
        for i in string:
            if i.isalpha() == False:
                palabras_incorrectas += 1
        if palabras_incorrectas != 0 :
            print("Ingrese un mensaje valido, sin numeros ni caracteres especiales")
    return ' '.join(string)  #volvemos a unir los elementos de la lista en un string y lo retornamos
        
if __name__ == '__main__':
    opcion = ingresar_opcion("Digite \"d\" si desea decodificar un mensaje o \"c\" si lo desea codificar ", "cd", 1)
    if opcion == 'c':
        mensaje_usuario = ingresar_alpha("Ingrese su mensaje a codificar (solo letras a-z): ")
        clave = ingresar_numero_entero_positivo("Ingrese su clave o desplazamiento: ")
        codificado = codificar(mensaje_usuario, clave)
    if opcion == 'd':
        mensaje_usuario = ingresar_alpha("Ingrese su mensaje codificado (solo letras a-z): ")
        clave = ingresar_numero_entero_positivo("Ingrese su clave o desplazamiento: ")
        codificado = decodificar(mensaje_usuario, clave)
