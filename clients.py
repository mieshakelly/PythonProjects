#!/usr/bin/env python


import mysql.connector
import cgitb

cnx = mysql.connector.connect(user='alexan12_wp5_pythonconnect', password='Slhs72td!!!',
															host='203.170.84.9',
															database='alexan12_wp5')
mycursor = cnx.cursor()

mycursor.execute("select name,dog_name,address from wp_acupet_clients order by name asc")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)
mycursor.close()
cnx.commit()

cnx.close()
