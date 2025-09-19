from datetime import datetime

hora_actual = datetime.now().hour
if hora_actual < 12:
    saludo = "Buenos días Antonio"
elif 12 <= hora_actual < 20:
    saludo = "Buenas tardes Antonio"
else:
    saludo = "Buenas noches Antonio"
print(saludo)