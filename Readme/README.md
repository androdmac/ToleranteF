##🐍 Manejo de Errores en Python - Parte 2

Autor: Andrea Rodriguez Macias
Asignatura: Computación Tolerante a Fallas

#🌟 Descripción

Este programa enseña cómo manejar errores en Python usando try-except y ZeroDivisionError.
Incluye ejemplos interactivos para practicar manejo de errores y crear código robusto y tolerante a fallos ⚡.

✍️ Ejemplo 1: Número con letras

📌 Solicita al usuario un número escrito solo con letras (ej. uno, dos).
❗ Si se ingresa un valor inválido, se lanza un ValueError personalizado.

Ingresa un numero escrito solo con letras: cuatro
✅ Número ingresado: cuatro

➗ Ejemplo 2: División segura

📌 Pide un número entero y calcula 10 / numero.
Manejo de errores específico:

Error	Mensaje mostrado
ValueError	"Ingresa un número válido."
ZeroDivisionError	"¡Ingresaste un dato no válido!, no puedes dividir entre cero"
Ingresa un numero: 2
✅ El resultado es: 5.0

🏃‍♂️ Cómo funciona

Intento de ejecución (try): El programa ejecuta el bloque de código que puede generar errores.

Captura de errores (except): Se manejan los errores según su tipo, mostrando mensajes claros.

Continuidad: El programa no se detiene ante entradas inválidas y sigue funcionando normalmente.

💡 Notas

try-except permite escribir programas robustos y tolerantes a fallos.

Se pueden usar múltiples except para manejar distintos tipos de errores.

Los mensajes de error personalizados ayudan a que el usuario entienda lo que hizo mal.
