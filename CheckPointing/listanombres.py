import pickle
import os

CHECKPOINT_FILE = "gestor_listas_checkpoint.pkl"

class GestorListas:
    def __init__(self):
        self.listas = {}  # Diccionario: nombre_lista -> lista de nombres

def guardar_estado(estado):
    """Guarda automáticamente el estado completo del gestor de listas."""
    with open(CHECKPOINT_FILE, "wb") as f:
        pickle.dump(estado, f)
    print("Estado guardado automáticamente.")

def cargar_estado():
    """Carga el estado desde el checkpoint si existe, sino crea uno nuevo."""
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "rb") as f:
            estado = pickle.load(f)
        print("Estado restaurado desde el punto de control.")
        return estado
    else:
        print("No se encontró punto de control. Se inicia un nuevo gestor de listas.")
        return GestorListas()

def eliminar_estado():
    """Elimina todo el archivo de checkpoint."""
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
        print("Archivo de checkpoint eliminado.")
    else:
        print("No existe archivo de checkpoint para eliminar.")

def main():
    estado = cargar_estado()
    
    try:
        while True:
            print("\n--- MENÚ CHECKPOINTING ---")
            print("--- LISTA DE NOMBRES ---\n")
            print("1. Crear nueva lista")
            print("2. Agregar nombre a lista")
            print("3. Ver listas y contenido")
            print("4. Eliminar lista")
            print("5. Eliminar estado completo")
            print("6. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre_lista = input("Nombre de la nueva lista: ").strip()
                if nombre_lista and nombre_lista not in estado.listas:
                    estado.listas[nombre_lista] = []
                    print(f"Lista '{nombre_lista}' creada.")
                    guardar_estado(estado)
                else:
                    print("[Nombre inválido o lista ya existe.")

            elif opcion == "2":
                nombre_lista = input("Lista a la que agregar: ").strip()
                if nombre_lista in estado.listas:
                    nombre = input("Nombre a agregar: ").strip()
                    if nombre:
                        estado.listas[nombre_lista].append(nombre)
                        print(f"Nombre '{nombre}' agregado a '{nombre_lista}'.")
                        guardar_estado(estado)
                    else:
                        print("Nombre vacío no agregado.")
                else:
                    print("Lista no encontrada.")

            elif opcion == "3":
                if not estado.listas:
                    print("No hay listas almacenadas.")
                for lista, nombres in estado.listas.items():
                    print(f"\nLista '{lista}':")
                    for idx, nombre in enumerate(nombres, 1):
                        print(f"{idx}. {nombre}")

            elif opcion == "4":
                nombre_lista = input("Nombre de la lista a eliminar: ").strip()
                if nombre_lista in estado.listas:
                    del estado.listas[nombre_lista]
                    print(f"Lista '{nombre_lista}' eliminada.")
                    guardar_estado(estado)
                else:
                    print("Lista no encontrada.")

            elif opcion == "5":
                eliminar_estado()
                estado = GestorListas()  # Reinicia el estado en memoria

            elif opcion == "6":
                print("Saliendo del programa...")
                guardar_estado(estado)
                break

            else:
                print("Opción inválida. Intenta nuevamente.")

    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")
        guardar_estado(estado)
        print("Estado final guardado. Puedes reanudar más tarde.")

if __name__ == "__main__":
    main()
