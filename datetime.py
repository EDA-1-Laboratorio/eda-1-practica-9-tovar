from datetime import datetime, timedelta

# Fecha y hora actual
ahora = datetime.now()
print("Ahora:", ahora)
print("Año:", ahora.year)
print("Mes:", ahora.month)
print("Día:", ahora.day)
print("Hora:", ahora.hour)

# Formatear fecha (como strftime en C)
print("Formato personalizado:", ahora.strftime("%d/%m/%Y %H:%M"))
# Ejemplo: 17/04/2026 14:30

# Calcular diferencia entre fechas
nacimiento = datetime(2006, 3, 15)
diferencia = ahora - nacimiento
print(f"Días de vida: {diferencia.days}")
print(f"Años aproximados: {diferencia.days // 365}")

# Sumar tiempo
manana = ahora + timedelta(days=1)
print("Mañana:", manana.strftime("%d/%m/%Y"))

proxima_semana = ahora + timedelta(weeks=1)
print("Próxima semana:", proxima_semana.strftime("%d/%m/%Y"))