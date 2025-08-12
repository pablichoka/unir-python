class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")           
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El nuevo precio no puede ser negativo")
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La nueva cantidad no puede ser negativa")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"Este es el producto {self.nombre}, del cual tenemos {self.cantidad} unidad/es y cada unidad cuesta {self.precio} euros."
    
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("El producto debe ser una instancia de la clase Producto")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return
    
    def calcular_valor_inventario(self):
      precios = []
      for producto in self.productos:
          precios.append(producto.calcular_valor_total())
      return sum(precios)
    
    def listar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos en el inventario")
        else:
          for producto in self.productos:
            print(producto)

def menu_principal():
    
    inventario = Inventario()

    while True:

      print("¿Que le gustaría hacer?")
      print ("1) Agregar un producto")
      print ("2) Buscar un producto")
      print ("3) Calcular el valor del inventario")
      print ("4) Listar productos")
      print ("5) Salir")
      election = input("Ingrese el numero con la operacion que desea realizar: ")

      if election not in ["1", "2", "3", "4", "5"]:
        raise ValueError("Opción no válida. Por favor, ingrese un número del 1 al 5.")
      
      if election == "1":
          try:
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            producto = Producto(nombre, precio, cantidad)
            inventario.agregar_producto(producto)
            print("Producto agregado exitosamente.")
          except ValueError as e:
              print(f"Error al agregar producto: {e}")
          except TypeError as e: # Para capturar el error si no es un Producto
              print(f"Error al agregar producto: {e}")
      elif election == "2":
          nombre = input("Ingrese el nombre del producto a buscar: ")
          producto = inventario.buscar_producto(nombre)
          if producto:
              print("Producto encontrado:")
              print(producto)
          else:
              print(f"No se encontró el producto '{nombre}'.")
      elif election == "3":
          valor_total = inventario.calcular_valor_inventario()
          print(f"El valor total del inventario es de {valor_total:.2f} euros.") # Formateado a 2 decimales
      elif election == "4":
          inventario.listar_productos()
      elif election == "5":
          print("Saliendo del programa. ¡Hasta luego!")
          break
    
if __name__ == "__main__":
    menu_principal()