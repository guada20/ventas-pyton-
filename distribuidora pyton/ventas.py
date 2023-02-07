dias_semana=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
nombre=[]
ventas_vendedor=[]

while True:
       Num_vendedor = int(input("Ingresa numero de vendedores"))
       if Num_vendedor>0: break
#ingreso nombre y ventas
for i_vendedor in range (0,Num_vendedor):
    nombre.append(input("ingresa nombre del vendedor %d:"%(i_vendedor + 1)))

    #ventas por dia
    ventas_dias=[]
    for i_dias in range(0,6):
        ventas_dias.append(int(input("cuanto vendio el %s" % dias_semana[i_dias])))
    ventas_vendedor.append(ventas_dias)
#recorro para ventas por vendedor
TotalVentasVendedor=[]
for ventas in ventas_vendedor:
    TotalVentasVendedor.append(sum(ventas))
#mostrando info
for nombre, ventas in zip(nombre, TotalVentasVendedor):
    print("%s ha vendido %d" % (nombre, ventas))

#porcentaje e ventas 
#porcentaje =[]
#for tv in
#mostrar 
#for n_v vt in zip(nombre, porcentaje):
#primt %s obtuvo un porcentaje de %d (nombre, porcentaje)
