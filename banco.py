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
    
    #CREAMOS UN METODO DE TRANSEFERENCIA ENTRE DOS USUARIOS
def transferencia(origen, destino, cantidad, fecha):
    if origen.verSaldo() >= cantidad:
        origen.reintegro(cantidad, fecha)
        destino.ingreso(cantidad, fecha)
        print(f"Transferencia exitosa de {cantidad} € de {origen.verCliente()} a {destino.verCliente()}")
    else:
        print(f"Fondos insuficientes en la cuenta de {origen.verCliente()} para realizar la transferencia.")

#CREAMOS UN PAR DE CLIENTES PARA PROBAR LA FUNCIONALIDAD DE LA CLASE
if __name__ == "__main__":
    cliente1 = Cuenta("Juan Perez", "10-02-2021")
    cliente2 = Cuenta("Maria Lopez", "23-08-2019")

    cliente1.ingreso(10000.0, "10-01-2022")
    cliente2.ingreso(10000.0, "14-05-2020")

    print(f"Cliente: {cliente1.verCliente()}, Saldo: {cliente1.verSaldo()} €")
    print(f"Cliente: {cliente2.verCliente()}, Saldo: {cliente2.verSaldo()} €")

    transferencia(cliente1, cliente2, 4500.0, "03-12-2023")

    print(f"Cliente: {cliente1.verCliente()}, Saldo: {cliente1.verSaldo()} €")
    print(f"Cliente: {cliente2.verCliente()}, Saldo: {cliente2.verSaldo()} €")

    