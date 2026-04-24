from modelos import Gasto, GestorGastos, CATEGORIAS
from utilidades import pedir_numero, pedir_texto, separador
from datetime import datetime

def menu_agregar(gestor: GestorGastos) -> None:
    separador("Agregar gasto")

    descripcion = pedir_texto("Descripcion: ", min_largo=3)

    monto = pedir_numero("Mont ($): ", minimo=1)

    print("\nCategorias disponibles:")
    for i, cat in enumerate(CATEGORIAS, 1):
        print(f" {i}, {cat}")

    while True:
        try:
            opcion = int(input("\nElige categoría (número): "))
            if 1 <= opcion <= len(CATEGORIAS):
                categoria = CATEGORIAS[opcion -1]
                break
            print(f"Elige entre 1 y {len(CATEGORIAS)}")
        except ValueError:
            print("Ingresa un número")

    gasto = Gasto(descripcion, monto, categoria)
    gestor.agregar(gasto)

def menu_listar(gestor: GestorGastos) -> None:
    separador("Mis gastos")

    if not gestor.gastos:
        print("No hay gastos registrados")
        return
    for i, gasto in enumerate(gestor.gastos):
        print(f" [{i}] {gasto}")

    print(f"\n{'-'*50}")
    print(f" TOTAL: ${gestor.total():>15,.0f} COP")
    print(f" Gastos registrados: {len(gestor)}")

def menu_por_categoria(gestor: GestorGastos) -> None:
    separador("Gastos por categoría")

    if not gestor.gastos:
        print("No hay gastos registrados")
        return

    por_cat = gestor.por_categoria ()
    total_general = gestor.total()

    for categoria, datos in sorted(por_cat.items()):
        total_cat = datos["total"]
        porcentaje = (total_cat / total_general * 100) if total_general > 0 else 0
        barra = "Aprobado" * int(porcentaje/5)
        print(f"\n {categoria.upper()}")
        print(f" Total: ${total_cat:,.0f} COP ({len(datos['gastos'])} gastos)")

def menu_eliminar(gestor: GestorGastos) -> None:
    separador("Eliminar gasto")

    if not gestor.gastos:
        print("No hay gastos para eliminar")
        return
    menu_listar(gestor)
    try:
        indice = int(input("\n¿Qué indice eliminar? "))
        confirmar = input(f"¿Seguro? (s/n): ")
        if confirmar.lower() == "s":
            gestor.eliminar(indice)
        else:
            print("Cancelado")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def menu_resumen_mes(gestor: GestorGastos) -> None:
    separador("Resumen del mes actual")
    ahora = datetime.now()
    gastos_mes = gestor.del_mes(ahora.year, ahora.month)

    if not gastos_mes:
        print(f"No hay gastos en {ahora.strftime('%B %Y')}")
        return
    total_mes = sum(g.monto for g in gastos_mes)
    print(f"Mes: {ahora.strftime('%B %Y')}")
    print(f"Gastos: {len(gastos_mes)}")
    print(f"Total: ${total_mes:,.0f} COP\n")

    for gasto in gastos_mes:
        print (f" {gasto}")

def mostrar_menu() -> str:
    separador("Calculadora de Gastos")
    print("  1. Agregar gasto")
    print("  2. Ver todos los gastos")
    print("  3. Ver por categoría")
    print("  4. Resumen del mes")
    print("  5. Eliminar gasto")
    print("  6. Salir")
    return input("\nOpción: ").strip()


def main():
    print(" Calculadora de Gastos Personales")
    print("Tu dinero bajo control\n")

    gestor = GestorGastos()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            menu_agregar(gestor)
        elif opcion == "2":
            menu_listar(gestor)
        elif opcion == "3":
            menu_por_categoria(gestor)
        elif opcion == "4":
            menu_resumen_mes(gestor)
        elif opcion == "5":
            menu_eliminar(gestor)
        elif opcion == "6":
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print( "Opción no válida")

if __name__ == "__main__":
    main()
            