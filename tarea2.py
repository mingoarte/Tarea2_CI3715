from datetime import *
import datetime
class Tarifa(object):

	def __init__(self, tasa_dias_semana, tasa_fines_semana):
		self.tasa_dias_semana = tasa_dias_semana
		self.tasa_fines_semana = tasa_fines_semana
		
format = '%d-%m-%Y %H:%M'

print('En que fecha entraste a trabajar? Introduce los datos sin espacio')
fecha_entrada = input('Ej. 24-05-2011 23:44 \n')
fecha_entrada = datetime.datetime.strptime(fecha_entrada, format)



print('En que fecha saliste del trabajo? Introduce los datos sin espacio')
fecha_salida = input('Ej. 24-05-2011 23:44 \n')
fecha_salida = datetime.datetime.strptime(fecha_salida, format)

print(fecha_salida.time().hour)

dias_semana = 0
dias_fin_semana = 0


for x in range(0,(fecha_salida - fecha_entrada).days):
	dia = fecha_entrada + timedelta(x + 1)

	if dia.weekday() >= 5:
		
		dias_fin_semana = dias_fin_semana + 1
		print('Fin de semana ',dia)

	else:
		dias_semana = dias_semana + 1
		print('Dia de semana',dia)


total = dias_semana + dias_fin_semana




print('Los dias de la semana son ', dias_semana)
print('Los dias del fin de semana son ', dias_fin_semana)






