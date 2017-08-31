#!C:/Python27/python.exe
   
import cgi,cgitb
import sqlite3
import json
import datetime
import time
  
cgitb.enable() #for debugging  
form = cgi.FieldStorage()  

result = {}
if form.has_key('Add'):
	user_input = form['Add']
	if validate_iput(user_input):
		result = add_appointment(user_input)
	else:
		return "Invalid input"
elif form.has_key('Search'):
	appointments_str = form['Search']
	result = get_appointments(appointments)
return result

def validate_input(input):
	appt_date = input[0]
	appt_time = input[1]
	
	if appt_time < time.strftime("%x"): #less than current date
		return False
	elif appt_time == datetime.date.today() and appt_time <= time.strftime("%X"): #today's date but less than current time
		return False
	return True

def get_appointments(input):
	conn = sqlite3.connect("appointments.db") 
	c = conn.cursor()
	c.execute(SELECT date, description FROM appointments WHERE description LIKE%(?)%", input)
	rows = c.fetchall()
	conn.close()
	return json.dumps(rows) 
	
def add_appointment(input):
	conn = sqlite3.connect("appointments.db")
	c = conn.cursor()
	appt_date = input[0]
	appt_time = input[1]
	description = input[2]
	appt_datetime = datetime.datetime.combine(datetime.date(appt_date), datetime.time(appt_time))
	try:
		c.execute("INSERT into appointments (date, time, description) VALUES (?,?,?)", appt_datetime, description)
	except sqlite3.Error as er:
		return json.dumps(err)
	c.commit()
	c.close()


