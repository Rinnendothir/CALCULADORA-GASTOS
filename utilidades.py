def pedir_numero(mensaje: str, minimo: float = None, maximo: float = None) -> float:
    """Pide un número válido al usuario con validación"""
    while True:
        try:
            numero = float(input(mensaje))
            if minimo is not None and numero < minimo:
                print(f"Debe ser >= {minimo}")
                continue
            if maximo is not None and numero > maximo:
                print(f"Debe ser <= {maximo}")
                continue 
            return numero
        except ValueError:
            print("Ingresa un número válido.")

def pedir_texto(mensaje: str, min_largo: int = 1) -> str:
    """Pide un texto válido al usuario con validación"""
    while True:
        texto = input(mensaje).strip()
        if len(texto) >= min_largo:
            return texto
        print(f"El texto debe tener al menos {min_largo} caracteres.")

def limpiar_pantalla() -> None:
    """Limpia la terminal"""
    import os
    os.system("cls" if os.name == "nt" else "clear")

def separador(titulo: str = "", largo: int = 40) -> None:
    """Imprime un separador con un título opcional"""
    if titulo:
        print(f"\n{'-' * 5} {titulo} {'-' * (largo - len(titulo) - 7)}")
    else:
        print("-" * largo)

def formatear_pesos(cantidad: float) -> str:
    """Formatea una cantidad como pesos colombianos"""
    return f"${cantidad:,.2f} COP"   
