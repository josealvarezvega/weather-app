import os
from docxtpl import DocxTemplate

 

nombre_del_producto = 'factura'
cantidad_precio_hora = int('52')
cantidad_hora_dia = int('8')
cantidad_dia_mes = int(input('Cantidad días :'))
subtotal = float(cantidad_dia_mes * (cantidad_hora_dia * cantidad_precio_hora))
porcentaje_de_impuesto = float(21/100)
total_impuesto = float(subtotal * porcentaje_de_impuesto)
round (2)
total = float(subtotal + total_impuesto)

print (nombre_del_producto)
print('Número de días facturados')
print (cantidad_dia_mes)
print ('Cantidad sin IVA')
print (subtotal)
print (porcentaje_de_impuesto)
print ('IVA')
print (total_impuesto)
print ('total con IVA')
print (total)



doc = DocxTemplate("factura_prueba.docx")
context = { 'factura' : 'PX-2202', 'dias' : cantidad_dia_mes, 'tarifa_dia' : cantidad_precio_hora, 'cantidad_neta' : subtotal, 'cantidad_neta' : subtotal, 'iva' : total_impuesto, 'total_Factura' : total }
doc.render(context)
doc.save("mysite/mysite/static/" + input('Ingrese nombre del archivo : ') + ".docx")




os.system('pause')
