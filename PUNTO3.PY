#Clase Aserradero - 
def obtainUtility()-> float:
    companies = Aserradero.get__empresasasociadas()
    for companie in companies:
        if (companie.get__is_cliente())==True:
        pass

#Clase Empresa
def obtainEarningsCustomer(cliente: Empresa)->float:
    ganancia = 0
    facturas = cliente.get__facturas()
    for factura in facturas:
        
    pass
