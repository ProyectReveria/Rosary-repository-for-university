#si la compra es mayor a 100 dolares darle un descuento del 10%

def descuentoaplicado():
    valor_Compras = int(input("Estimado usuario ingrese el costo de su pedido"))
    if valor_Compras >= 100: 
        Valor_Descuento = valor_Compras * 0.90
        print(F"Su descuento si aplica, el precio es de {Valor_Descuento}")
    else:
        print(F"su descuento no aplica, el precio es de {valor_Compras}")

descuentoaplicado()