import random

def generar_password():
    mayusculas = ["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    minusculas = ["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    simbolos = ["!","#","$","&","/","(",")","¡"]
    numeros = ["0","1","2","3","4","5","6","7","8","9"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres) #selecciona un valor aleatorio de una lista
        contrasena.append(caracter_random)

    #convertir una lista en un string
    contrasena = "".join(contrasena)

    return contrasena

def run():
    contrasena = generar_password()
    print("Tu nueva contrasena es: " + contrasena)

if __name__ == "__main__":
    run()