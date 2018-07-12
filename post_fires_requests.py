import requests
import sqlite3

conexion = sqlite3.connect("/home/jesus-alfonso/Documentos/Examen_continental/USWildfires.sqlite")
cursor = conexion.cursor()
cursor.execute("select DISTINCT FIRE_YEAR,max(FIRE_SIZE),FIRE_NAME from Fires GROUP BY FIRE_YEAR order by FIRE_YEAR ASC")
registros = cursor.fetchall()
diccionario = {}
fire_year = []
fire_size = []
fire_name = []
for reg in registros:
	fire_year.append(reg[0])
	fire_size.append(reg[1])
	fire_name.append(reg[2])
	diccionario = {
		'FIRE_YEAR' : fire_year,
		'FIRE_SIZE' : fire_size,
		'FIRE_NAME' : fire_name
	}
url = "http://ptsv2.com/t/lp3vp-1531189579/post"

r = requests.post(url=url, data=diccionario)

print("URL:%s"%format(r.url))
print("status code:%s"%format(r.status_code))
print("Text Output:\n %s"%format(r.text))
print("headers Output:\n %s"%format(r.headers))