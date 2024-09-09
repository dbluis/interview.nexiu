# Modo historico: Si restando 2 años a la fecha no da = a el ultimo dia del mes entonces la fecha pasa a ser el 1 del mes siguiente
# Si restando 2 años esta da igual al ultimo dia del mes entonces esta empieza el primero de ese mismo mes

# Modo Programado: La fecha siempre sera el 1er dia del mes anterior y la fecha final sera el final de ese mismo mes

from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar


def rangoDeFechas(tipo, fecha):
    fecha_convertida = datetime.strptime(fecha, "%d/%m/%Y")

    def ultimo_dia_mes(fecha):
        return calendar.monthrange(fecha.year, fecha.month)[1]

    if tipo == "historico":

        fecha_inicio = fecha_convertida - relativedelta(years=2)

        ultimo_dia = ultimo_dia_mes(fecha_inicio)

        if fecha_inicio.day != ultimo_dia:
            dias = ultimo_dia - fecha_inicio.day
            fecha_inicio = fecha_inicio + relativedelta(days=dias + 1)

        else:
            fecha_inicio = fecha_inicio.replace(day=1)

        fecha_final = fecha_convertida - relativedelta(month=1)
        ultimo_dia_final = ultimo_dia_mes(fecha_final)
        fecha_final = fecha_final.replace(day=ultimo_dia_final)

    elif tipo == "programado":

        fecha_inicio = fecha_convertida.replace(
            day=1) - relativedelta(months=1)
        ultimo_dia = ultimo_dia_mes(fecha_inicio)
        fecha_final = fecha_inicio.replace(day=ultimo_dia)

    diccionario_fechas = []
    fecha_actual = fecha_inicio
    while fecha_actual <= fecha_final:

        primer_dia = fecha_actual.replace(day=1)
        ultimo_dia = fecha_actual.replace(ultimo_dia_mes(fecha_actual))

        diccionario_fechas.append({
            "fecha inicio": primer_dia.strftime("%d/%m/%Y"),
            "fecha finalizacion": ultimo_dia.strftime("%d/%m/%Y")
        })

        fecha_actual = fecha_actual + relativedelta(months=1)
    return diccionario_fechas


resultado = rangoDeFechas("historico", "30/09/2024")

for i in resultado:
    print(i)
