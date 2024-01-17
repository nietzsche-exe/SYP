from banco import Cuenta

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