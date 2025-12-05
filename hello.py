from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


p: Product = Product("Laptop", 99.9)
