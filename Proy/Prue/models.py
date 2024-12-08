from django.db import models

class Categorias(models.Model):
    id_categorias = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)

    def _str_(self): 
        return self.nombre


class Productos(models.Model):
    id_productos = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return self.nombre


class Clientes(models.Model):
    id_clientes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"


class Pedidos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20, 
        choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')]
    )

    def _str_(self):
        return f"Pedido {self.id} de {self.cliente.nombre}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"Detalle de {self.producto.nombre} en pedido {self.pedido.id}"


class Facturas(models.Model):
    id_facturas = models.CharField(max_length=10, primary_key=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=20)

    def _str_(self):
        return f"Factura {self.id_facturas} - Monto total: {self.monto_total}"
