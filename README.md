# ☕ Cafetería Proyecto Final

Este proyecto es una solución integral para la gestión de una cafetería, desarrollada bajo una **arquitectura de microservicios** distribuida. [cite_start]Utiliza tecnologías modernas para garantizar la escalabilidad, el aislamiento de procesos y un despliegue eficiente mediante contenedores.

---

## 🏗️ Arquitectura del Sistema

[cite_start]El ecosistema se compone de varios microservicios independientes que se comunican a través de APIs REST con soporte para CORS:

| Microservicio | Puerto | Descripción |
| :--- | :--- | :--- |
| **`usuarios-service`** | `5002` | [cite_start]Gestión de perfiles, autenticación y roles de personal[cite: 1, 10]. |
| **`pedidos-service`** | `5001` | [cite_start]Registro, procesamiento y seguimiento de órdenes[cite: 8]. |
| **`inventario-service`** | `5003` | [cite_start]Control de existencias, productos y alertas de stock[cite: 6]. |
| **`notificaciones-service`** | `5004` | [cite_start]Envío de alertas y estados de pedido en tiempo real. |

---

## 🚀 Tecnologías Utilizadas

* [cite_start]**Backend:** [Python 3.11](https://www.python.org/) con [Flask](https://flask.palletsprojects.com/)[cite: 6, 7, 8].
* [cite_start]**Seguridad:** [Flask-CORS](https://flask-cors.readthedocs.io/) para comunicación segura entre servicios[cite: 9, 10].
* [cite_start]**Contenedores:** [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)[cite: 1, 10].
* [cite_start]**Orquestación:** [Kubernetes](https://kubernetes.io/) (K8s).

---

## 🛠️ Guía de Inicio Rápido

### 1. Requisitos Previos
* [cite_start]Docker Desktop y Docker Compose instalados.
* [cite_start]Kubernetes habilitado (Minikube o Docker K8s).

### 2. Despliegue con Docker Compose
Desde la raíz del proyecto, ejecuta el siguiente comando para levantar toda la infraestructura:
```bash
docker-compose up --build