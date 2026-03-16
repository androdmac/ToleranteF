<p align="center">
# (Par. 1) Otras herramientas para el manejar errores
  
Computación Tolerante a Fallas 2026A
Andrea Rodríguez Macias
Centro Universitario de Ciencias Exactas e Ingenierías CUCEI, Ingeniería en Computación, Guadalajara, Jalisco
andrea.rodriguez5028@alumnos.udg.mx
</p>

------------------------------------------------------------------------------------------------------------------------------------------

El objetivo de las herramientas para el manejo de errores no es meramente registrar un fallo, si no encontrar rastro del fallo, 
más implicitamente la linea exacta del codigo donde se presento el error permitiendo solucionar el fallo de una manera más sencilla.

## Herramienta
### 🛡️Sentry:
* Captura la excepción y revela qué variables locales estaban presentes en el momento del fallo.
### Especialidad
* Equipos que necesitan visibilidad total desde el backend (Python, Node, Go) hasta el frontend (React, Vue) y móviles.

### ✨Rollbar:
* Brilla cuando despliegas código constantemente. Se integra con tus herramientas de despliegue para decirte en qué versión exacta (commit) 
se introdujo el bug, basicamente análisis de regresión (detecta si un error viejo volvió).
### Especialidad
* Integración Continua (CI/CD)

### 🕵️LogRocket:
* A veces el error no es una excepción técnica, sino un error de lógica o UX. 
LogRocket graba la sesión del usuario (red, consola, DOM) para que puedas reproducir el error sin adivinar, permite "ver" un video de
lo que hizo el usuario antes del error.
### Especialidad
* Desarrolladores Frontend y Product Managers.
* Session Replay

### ⚡Raygun:
* Vincula errores directamente con la experiencia del cliente.
### Especialidad
* Monitoreo de Usuario Real (RUM).

### 🪂Airbrake: 
* Muy ligero y fácil de configurar en apps pequeñas/medianas.
### Especialidad
* Simplicidad y Enfoque Dev.
------------------------------------------------------------------------------------------------------------------------------------------

