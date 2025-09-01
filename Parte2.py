#Ejemplo: Otras herramientas para el manejar errores Parte 2
#Andrea Rodriguez Macias
#Computación Tolerante a Fallas


#Usando try-except
def ejemplo1():
    try:
        numero = input("Ingresa un numero escrito solo con letras: ")
        if not numero.isalpha():
            raise ValueError("¡Ingresaste un dato no valido!, ingresa el numero solo con letras")
        print(f"Número ingresado: {numero}")
    except ValueError as e:
        print(f"¡Error! {e}")

#Usando try-except-zerodivisionerror
def ejemplo2():
    try:
        numero = int(input("Ingresa un numero: "))
        resultado = 10 / numero
        print(f"El resultado es: {resultado}")
    except ValueError:
        print("Ingresa un numero valido.")
    except ZeroDivisionError:
        print("¡Ingresaste un dato no valido!, no puedes dividir entre cero")


if __name__ == "__main__":
    print("\nEjemplo 1")
    ejemplo1()
    
    print("\nEjemplo 2")
    ejemplo2()
