from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
import os
from docxtpl import DocxTemplate
import comtypes.client
import pythoncom
import calendar
import time

def index(request):
    c = {}
    c.update(csrf(request))

    if request.method == 'POST':
        #Desglose de la factura
        cantidad_dia_mes = int(request.POST.get('cantidad_dia_mes', 0))
        nombre_del_producto = 'factura'
        cantidad_dia = float(request.POST.get('cantidad_dia', 0))
        subtotal = float(cantidad_dia_mes * (cantidad_dia))
        porcentaje_de_impuesto = float(21/100)
        total_impuesto = float(subtotal * porcentaje_de_impuesto)
        total = float(subtotal + total_impuesto)
        factura = request.POST.get('factura', '')
        fecha_factura = request.POST.get('fecha_factura', '')
        concepto_factura = request.POST.get('concepto_factura', '')
        
        # Emisor de la factura
        nombre_emisor_factura = request.POST.get('nombre_emisor_factura', '')
        documento_emisor_factura = request.POST.get('documento_emisor_factura', '')
        direccion_emisor_factura = request.POST.get('direccion_emisor_factura', '')
        telefono_emisor_factura = request.POST.get('telefono_emisor_factura', '')
        mail_emisor_factura = request.POST.get('mail_emisor_factura', '')
        nombre_de_banco_emisor_factura = request.POST.get('nombre_de_banco_emisor_factura', '')
        IBAN_emisor_factura = request.POST.get('IBAN_emisor_factura', '')
        
        # Receptor de la factura
        nombre_receptor_factura = request.POST.get('nombre_receptor_factura', '')
        documento_receptor_factura = request.POST.get('documento_receptor_factura', '')
        direccion_receptor_factura = request.POST.get('direccion_receptor_factura', '')
        telefono_receptor_factura = request.POST.get('telefono_receptor_factura', '')
        mail_receptor_factura = request.POST.get('mail_receptor_factura', '')

        
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)

        doc = DocxTemplate("factura_prueba.docx")
        context = {'factura': factura, 
                    
                   #Datos emisor de la factura 
                   'telefono_emisor_factura' : telefono_emisor_factura, 
                   'direccion_emisor_factura' : direccion_emisor_factura, 
                   'documento_emisor_factura' : documento_emisor_factura, 
                   'nombre_emisor_factura' : nombre_emisor_factura,
                   'telefono_emisor_factura' : telefono_emisor_factura,
                   'mail_emisor_factura' : mail_emisor_factura,
                   'nombre_de_banco_emisor_factura' : nombre_de_banco_emisor_factura,
                   'IBAN_emisor_factura' : IBAN_emisor_factura,


                   
                   #Datos receptor de la factura
                    'nombre_receptor_factura': nombre_receptor_factura,
                    'documento_receptor_factura' : documento_receptor_factura,
                    'direccion_receptor_factura' : direccion_receptor_factura,
                    'telefono_receptor_factura' : telefono_receptor_factura,
                    'mail_receptor_factura' : mail_receptor_factura,



                   #Datos desglose de la afctura
                   'fecha_factura' : fecha_factura,
                   'concepto_factura' : concepto_factura, 
                   'dias': cantidad_dia_mes, 
                   'tarifa_dia': f"{cantidad_dia:.2f}€".replace(".", ","), 
                   'cantidad_neta': f"{subtotal:.2f}€".replace('.', ','),
                   'iva': f"{total_impuesto:.2f}€".replace('.', ','),
                   'total_Factura': f"{total:.2f}€".replace('.', ',')
}
        doc.render(context)
     
        ruta_word = str(time_stamp) + ".docx"
        ruta_pdf = str(time_stamp) + ".pdf"
        doc.save(ruta_word)
        
        # Conversión a PDF
        pythoncom.CoInitialize()
        wdFormatPDF = 17
        in_file = os.path.abspath(ruta_word)
        out_file = os.path.abspath(ruta_pdf)
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
        pythoncom.CoUninitialize()
        
        # Descarga en el navegador
        with open(ruta_pdf, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + ruta_pdf
            
            # Cerrar el archivo
            pdf.close()

            os.remove(ruta_word)
            os.remove(ruta_pdf)
            return response
            
    
    else:
        return render(request, 'index.html', c)