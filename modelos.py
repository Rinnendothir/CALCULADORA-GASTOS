
import json
from datetime import datetime

ARCHIVO = "gastos.json"

CATEGORIAS = [
    "alimentacion",
    "transporte",
    "educacion",
    "entretenimiento",
    "salud",
    "ropa",
    "servicios",
    "otro"
]

class Gasto:
    """Representa un gasto individual."""

    def __init__(self, descripcion: str, monto: float,
                categoria: str, fecha: str = None):
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria.lower()
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self) -> dict:
        return {
            "descripcion": self.descripcion,
            "monto": self.monto,
            "categoria": self.categoria,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Gasto":
        return cls(
            descripcion=datos["descripcion"],
            monto=datos["monto"],
            categoria=datos["categoria"],
            fecha=datos["fecha"]
        )

    def __str__(self) -> str:
        return (f"[{self.fecha}] {self.descripcion:25} " +
                f"${self.monto:>10,.0f} {self.categoria}")


class GestorGastos:
    """Maneja la coleccion completa de gastos."""

    def __init__(self):
        self.gastos: list[Gasto] = []
        self.cargar()

    def cargar(self) -> None:
        """Carga los gastos desde el archivo JSON."""
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.gastos = [Gasto.from_dict(d) for d in datos]
        except OSError:
            self.gastos = []

    def guardar(self) -> None:
        """Guarda los gastos en el archivo JSON."""
        try:
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                json.dump([g.to_dict() for g in self.gastos],
                          f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"Error al guardar: {e}")

    def agregar(self, gasto: Gasto) -> None:
        """Agrega un gasto a la lista."""
        self.gastos.append(gasto)
        self.guardar()

    def eliminar(self, indice: int) -> None:
        """Elimina un gasto por índice."""
        if not 0 <= indice < len(self.gastos):
            raise IndexError("Indice fuera de rango.")
        eliminado = self.gastos.pop(indice)
        self.guardar()
        print(f"Eliminado: {eliminado.descripcion}")

    def total(self) -> float:
        """Retorna el total de los gastos."""
        return sum(g.monto for g in self.gastos)

    def por_categoria(self) -> dict:
        """Agrupa los gastos por categoría con su total."""
        resultado = {}
        for gasto in self.gastos:
            cat = gasto.categoria
            if cat not in resultado:
                resultado[cat] = {"gastos": [], "total": 0}
            resultado[cat]["gastos"].append(gasto)
            resultado[cat]["total"] += gasto.monto
        return resultado

    def del_mes(self, año: int, mes: int) -> list:
        """Retorna los gastos de un mes específico."""
        prefijo = f"{año}-{mes:02d}"
        return [g for g in self.gastos if g.fecha.startswith(prefijo)]

    def __len__(self) -> int:
        return len(self.gastos)