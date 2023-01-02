#Importar el metodo choice -> para escoger una palabra al azar de una lista de palabras que se creara
#Funciones -> pedir letra, validar letra, chequear letras, ver si ganó
from random import choice
from os import system
def elegir_palabra(listaPalabras):
    """
    Esta funcion se encargará de escoger una palabra al azar de la lista de palabras creadas
    """
    palabra = choice(listaPalabras)
    return palabra

def validar_cadena(cadena):
    """
    Esta funcion se encarga de validar si cada ingreso por parte del usuario es
    un string
    """
    if cadena.isalpha():
        return True
    else:
        return False

def crear_lista_palabras(palabra):
    """
    Esta funcion recibe la palabra que se ha escogido al azar
    y crea una lista la cual estará conformada por cada una de
    las letras que componene a la palabra seleccionada.
    """
    newPalabra = []
    for e in palabra:
        newPalabra.append(e)
    return newPalabra

def crear_segmentos(palabra):
    """
    Esta funcion creará una lista con la cantidad de espacios requeridos
    para formar la palabra del juego, haciendo que cada letra de la palabra
    sea remplazada por un ' _ '. Despues de reemplazar cada palabra
    esta nueva cadena de '_' se retornará.

    """

    listSegmentos = []
    contador = 0
    for l in palabra:
        if palabra[contador] != ' ':
            listSegmentos.append(palabra[contador].replace(l,'_'))
            contador += 1
        else:
            contador +=1
            listSegmentos.append(' ')
            continue
    segmentos = "".join(listSegmentos)
    return segmentos

def letra_Correcta(nombre,listPalabras,vidas,segmentos):

    """
    Esta funcion se encargará de verificar si la letra que ingreso el usuario está
    dentro de la frase escogida por el programa al azar si es asi,
    recorrera toda la cadena en busca de esa letra y en la cadena que está
    compuesta de '_' reemplazará dicho espacio con la letra del usuario para así
    ir mostrandole como va completando la palabra.
    """
    contador = 0
    listSegmentos= list(segmentos)
    palabra = "".join(listPalabras)
    print(f"\nLa palabra se ve así: {segmentos}")
    #print(listSegmentos)
    while vidas != 0 and segmentos!=palabra:
        letra = input("\nIngresa una letra: ").lower()
        if len(letra) > 1:
            print("Has ingresado mas de una letra. Intenta de nuevo con solo una letra.")
        else:
            if validar_cadena(letra):
                if letra in palabra and letra != '':
                    print("\nHas adivinado una letra!")
                    for l in palabra:
                        if listPalabras[contador] == letra and listPalabras[contador] != ' ':
                            listSegmentos[contador] = letra
                        contador += 1
                    contador = 0
                    segmentos = "".join(listSegmentos)
                    print(f"La palabra va de esta manera: {segmentos}")
                else:
                    vidas -= 1
                    if vidas == 0:
                        return print(f"Ops! {nombre} se te acabaron las vidas la palabra era '{palabra}', gracias por jugar!")
                    else:
                        print(f"\nTe has equivocado la letra '{letra}' no se encuentra en la palabra. Te quedan {vidas} vidas")
                        print(f"La palabra va de esta manera: {segmentos}")

                # print(listSegmentos)
            else:
                print("Has ingresado un caracter invalido")

    else:
        if ' ' in palabra:
            return (f"\n{nombre} haz adivinado la frase! la frase era '{palabra}' Felicitaciones!")
        else:
            return (f"\n{nombre} haz adivinado la palabra! la palabra era '{palabra}' Felicitaciones!")

def iniciar_juego():
    """
    Esta funcion se encarga de iniciar el juego, aca se inicializan las variables
    que se necesitan para las demás funciones.
    También se definen tanto la lista de palabras como las vidas que tendra el jugador.
    :return:
    """
    listaPalabras = ['Destruccion', 'Anita lava la tina', 'Diomedes el mejor','Hueler','Trym']
    palabra = elegir_palabra(listaPalabras)
    vidas = 6
    segmentos = crear_segmentos(palabra)
    lisPalabras = crear_lista_palabras(palabra.lower())

    """
    Validamos que el nombre que haya ingresado el usuario tenga solo letras y si no es asi
    que ingrese de nuevo su nombre
    """
    nombre = input("Ingresa tu nombre: ")
    while not validar_cadena(nombre):
        print("Has ingresado un nombre invalido.")
        nombre = input("Por favor ingresa un nombre valido: ")
    else:
        print(f"\nHola {nombre}! bienvenido al juego de 'El Ahorcado'")
        print(f"{nombre} he escogido una frase o palabra al azar espero que puedas adivinarla. Buena suerte!")
        print(letra_Correcta(nombre, lisPalabras, vidas, segmentos))
        system('cls')


iniciar_juego()

