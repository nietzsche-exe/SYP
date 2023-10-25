class Cuenta:
    #DEFINIMOS LA CLASE
    def __init__(self, nombre, fecha):
        self.nombre_cliente = nombre
        self.numero_cuenta = str(hash(nombre))[-10:]
        self.saldo = 0.0
        self.movimientos = [{"fecha": fecha, "tipo de movimiento": "apertura", "cantidad": 0.0}]

    #METODO PARA SACAR DINERO DE LA CUENTA DEL USUARIO
    def reintegro(self, cantidad, fecha):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            self.movimientos.append({"fecha": fecha, "tipo de movimiento": "reintegro", "cantidad": cantidad})
        else:
            print("La cantidad debe ser mayor que cero y no puede exceder el saldo disponible.")
   
   #METODO PARA INGRESAR DINERO EN LA CUENTA DEL USUARIO
    def ingreso(self, cantidad, fecha):
        if cantidad > 0:
            self.saldo += cantidad
            self.movimientos.append({"fecha": fecha, "tipo de movimiento": "ingreso", "cantidad": cantidad})
        else:
            print("La cantidad debe ser mayor a 0.")

   
    #METODOS toString
    def verCliente(self):
        return self.nombre_cliente
    
    def verSaldo(self):
        return self.saldo
    

    