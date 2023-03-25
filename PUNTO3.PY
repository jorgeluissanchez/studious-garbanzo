#Clase Aserradero - 
def obtainUtility()-> float:
    ganacias_totales = 0
    egresos_totales = 0
    companies = Aserradero.get__empresasasociadas()
    for companie in companies:
        if (companie.get__is_cliente())==True:
            ganacias_totales += obtainEarningsCustomer(companie)
            
        pass

def searchInTableCustomer(dimensiones,tipo)->float:
    pass





#Clase Empresa
def obtainEarningsCustomer(cliente: Empresa)->float:
    ganancia_cliente = 0
    facturas = cliente.get__facturas()
    for factura in facturas:
        valor_en_tabla = searchInTableCustomer(factura.tipo_madera,factura.dimensiones)
        ganancia_factura = valor_en_tabla*factura.num_piezas
        ganacia_factura = ganacia_factura*1.18  
        ganancia_cliente += ganacia_factura
    return ganancia_cliente
