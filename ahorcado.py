import os
"""El programa debe preguntar al usuario la palabra a adivinar.
A partir de la palabra introducida debe crear una lista con los caracteres de la palabra"""

palabra_Incognita = input("\ninserte la palabra a adivinar: ")
palabra_Incognita = palabra_Incognita.upper()


os.system("cls")
print()
_caracteres = []
caracter_Oculto = []

# Metodo para transformar un STR a Lista:

for caracter in palabra_Incognita:
    _caracteres.append(caracter)
    caracter_Oculto.append("_")

print(f"La palabra a adivinar contiene esta cantidad de letras: {caracter_Oculto}")

# Metodo para definir la cantidad posibles errores:
cont = 0
while cont < 5:

    respuesta = input(f"\ninserte una letra que usted crea que esta en la palabra a adivinar: ")
    respuesta = respuesta.upper()


    if respuesta in _caracteres:

        # Metodo para contar los index de las respuestas correctas:

        list_Index = []
        count = 0
        while count < len(_caracteres):

            respuesta_bucle = _caracteres.index(respuesta)
            _caracteres.pop(respuesta_bucle)
            caracter_Oculto.pop(respuesta_bucle)
            list_Index.append(respuesta_bucle)

            if _caracteres.count(respuesta) > 0:
                count += 1
            else:
                break

        # Metodo para reestructurar las listas con los datos:
        list_Index.reverse()

        for i in list_Index:
            caracter_Oculto.insert(i, respuesta)
            _caracteres.insert(i, respuesta)
        print(caracter_Oculto)

        # Validacion para comprobar la victoria
        if caracter_Oculto.count("_") == 0:
            print("\nFelicidades\nGanaste")
            exit()


    else:
        print("la letra no estaba en la palabra")
        cont += 1

print(f"\nLo siento perdiste la palabra era:\n\n{_caracteres}")
