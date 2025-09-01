# 📝 Gestor de Listas con Checkpointing en Python

**Autor:** Andrea Rodriguez Macias  
**Asignatura/Proyecto:** Persistencia y Tolerancia a Fallas en Python

=======

## 📌 Descripción
Este programa es un **mini gestor de listas de nombres** que utiliza **checkpointing automático** con serialización (`pickle`) para garantizar que nunca pierdas tus datos.  
Permite crear, visualizar y eliminar listas, y **restaurar automáticamente** el último estado guardado si el programa se cierra inesperadamente ⚡.

=======

## ✍️ Funcionalidades principales
- 🆕 **Crear lista:** Crea una lista con un nombre único.  
- ➕ **Agregar nombres:** Agrega nombres a la lista deseada.  
- 👀 **Ver listas:** Muestra todas las listas y su contenido.  
- 🗑️ **Eliminar lista:** Borra una lista individual.  
- ❌ **Eliminar estado completo:** Borra todas las listas y el checkpoint.  
- 💾 **Checkpoint automático:** Cada cambio se guarda automáticamente.  
- 🔄 **Restauración del estado:** Recupera la última versión guardada al reiniciar.

=======

## 🏃‍♂️ Cómo funciona
# Ejemplo 1
Ingresa un numero escrito solo con letras: cuatro
✅ Número ingresado: cuatro

# Ejemplo 2
Ingresa un numero: 2
✅ El resultado es: 5.0

=======

### # Ejemplo 1 - Crear y agregar nombres
```
Ingresa el nombre de la lista: Amigos
Agrega un nombre: andrea
Agrega un nombre: erick
✅ Lista 'Amigos' actualizada: ['andrea', 'erick']
```

### # Ejemplo 2 - Ver listas
```
Lista 'Amigos':
1. andrea
2. erick
```

### # Ejemplo 3 - Eliminar lista
```
Ingresa la lista a eliminar: lista 1
✅ Lista 'lista 1' eliminada correctamente
```

### # Ejemplo 4 - Restauración automática
```
Reinicia el programa
✅ Último estado restaurado automáticamente desde el checkpoint
```
