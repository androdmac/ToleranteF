# 🐍 Manejo de Errores en Python - Parte 2

**Autor:** Andrea Rodríguez Macías  
**Asignatura:** Computación Tolerante a Fallas

---

## 🌟 Descripción

Este proyecto enseña cómo manejar errores en Python usando `try-except` y `ZeroDivisionError`. Incluye ejemplos interactivos para practicar la creación de **programas robustos y tolerantes a fallos** ⚡.

---

## ✍️ Ejemplo 1: Número con letras
📌 Solicita al usuario un número escrito solo con letras (ej. `uno`, `dos`). 

❗ Si se ingresa un valor inválido, se lanza un `ValueError` personalizado.

### 💻 Código de ejemplo
```
numero = input("Ingresa un número escrito solo con letras: ")
# Validación personalizada
if not numero.isalpha():
    raise ValueError("¡Ingresa un número válido escrito en letras!")
print(f"✅ Número ingresado: {numero}") 
```

---

### 🖥️ Ejecución esperada

Ingresa un número escrito solo con letras: cuatro

✅ Número ingresado: cuatro


➗ Ejemplo 2: División segura

📌 Pide un número entero y calcula 10 / número.

---

### ⚠️ Manejo de errores

ValueError --->	"Ingresa un número válido."

ZeroDivisionError ---> "¡Ingresaste un dato no válido!, no puedes dividir entre cero"

---

### 💻 Código de ejemplo
```
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"✅ El resultado es: {resultado}")
except ValueError:
    print("Ingresa un número válido.")
except ZeroDivisionError:
    print("¡Ingresaste un dato no válido!, no puedes dividir entre cero")
```
----

### 🖥️ Ejecución esperada
Ingresa un número: 2

✅ El resultado es: 5.0

---

### 🏃‍♂️ Cómo funciona
Try	---> Ejecuta el bloque de código que puede generar errores.

Except ---> Captura y maneja errores según su tipo, mostrando mensajes claros.

Continuidad	---> El programa sigue funcionando normalmente a pesar de entradas inválidas.
