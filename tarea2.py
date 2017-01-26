##
##Tarea 2
##Domingo Arteaga 11-10058
##Edgar Silva 
##


from datetime import *
import datetime
class Tarifa(object):

	def __init__(self, tasa_dias_semana, tasa_fines_semana):
		self.tasa_dias_semana = tasa_dias_semana
		self.tasa_fines_semana = tasa_fines_semana
		


def tiempoDeTrabajo(Tarifa,inicioDeServicio, finDeServicio):
	dias_semana = 0
	dias_fin_semana = 0
	
	for x in range(0,(finDeServicio - inicioDeServicio).days):
		dia = inicioDeServicio + timedelta(x + 1)

		if dia.weekday() >= 5:
			
			dias_fin_semana = dias_fin_semana + 1
			print('Fin de semana ',dia)

		else:
			dias_semana = dias_semana + 1
			print('Dia de semana',dia)


	if inicioDeServicio.date().weekday() >= 5:
		gasto_horas_entrada = (24 - int(inicioDeServicio.time().hour)) * Tarifa.tasa_fines_semana
	else: 
		gasto_horas_entrada = (24 - int(inicioDeServicio.time().hour)) * Tarifa.tasa_dias_semana


	if finDeServicio.date().weekday() >= 5:
		gasto_horas_salida = int(finDeServicio.time().hour) * Tarifa.tasa_fines_semana
	else: 
		gasto_horas_salida = int(finDeServicio.time().hour) * Tarifa.tasa_dias_semana


	total = gasto_horas_salida + gasto_horas_entrada + (dias_semana * 24 * Tarifa.tasa_dias_semana)\
								 + (dias_fin_semana * 24 * Tarifa.tasa_fines_semana)
	

	print('El monto total es: Bs. ', total)


precio_normal = input('Cual es la tarifa para los dias de semana?')
precio_fin_semana = input('Cual es la tarifa para los fines de semana?')

precios = Tarifa(int(precio_normal) , int(precio_fin_semana))


format = '%d-%m-%Y %H:%M'

print('En que fecha entraste a trabajar? Introduce los datos sin espacio')
fecha_entrada = input('Ej. 24-05-2011 23:44 \n')
fecha_entrada = datetime.datetime.strptime(fecha_entrada, format)



print('En que fecha saliste del trabajo? Introduce los datos sin espacio')
fecha_salida = input('Ej. 24-05-2011 23:44 \n')
fecha_salida = datetime.datetime.strptime(fecha_salida, format)




tiempoDeTrabajo(precios, fecha_entrada,fecha_salida)



