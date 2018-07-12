import sqlite3
import csv

conexion = sqlite3.connect("/home/jesus-alfonso/Documentos/Examen_continental/USWildfires.sqlite")
path_name = "/home/jesus-alfonso/Documentos/Examen_continental/wildfire_outputs/2008_fire.csv"
cursor = conexion.cursor()
cursor.execute("select * from Fires where FIRE_YEAR = 2008")
registros = cursor.fetchall()
with open(path_name, 'w') as archivo:
	file = csv.writer(archivo)
	file.writerows(registros)