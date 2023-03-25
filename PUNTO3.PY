#Clase Aserradero - 
def obtainUtility()-> float:
    ganacias_totales = 0
    egresos_totales = 0
    companies = Aserradero.get__empresasasociadas()
    for companie in companies:
        if (companie.get__is_cliente()):
            ganacias_totales += companie.ObtainEarningsCustomer()
        else:
            egresos_totales += companie.obtainSales()
        pass
    return ganacias_totales-egresos_totales

def companieStatus(companie:Empresa):
    if (companie.get__is_client):
        return companie.obtainEarningsCustomer
    else:
        return companie.obtainSales()
    



#Clase EmpresaCliente
def obtainEarningsCustomer(cliente: Empresa)->float:
    ganancia_cliente = 0
    facturas = cliente.get__facturas()
    for factura in facturas:
        valor_en_tabla = searchInTableCustomer(factura.tipo_madera,factura.dimensiones)
        ganancia_factura = valor_en_tabla*factura.num_piezas
        ganacia_factura = ganacia_factura*1.18  
        ganancia_cliente += ganacia_factura
    return ganancia_cliente

#Clase EmpresaProveedora
def obtainSales(proveedor :Empresa)->float:
    egresos_proveedor = 0
    ordenes = proveedor.get__ordenes()
    for orden in ordenes:
        valor_en_tabla =searchInSupplier(orden.edad_promedio,orden.tipo_arbol)
        egreso_orden = valor_en_tabla* orden.num_troncos
        egreso_orden = egreso_orden * 1.15
        egresos_proveedor += egreso_orden
    return egresos_proveedor

def searchInTableCustomer(dimensiones,tipo)->float:
    pass

def searchInSupplier(edad,tipo)->float:
 pass
