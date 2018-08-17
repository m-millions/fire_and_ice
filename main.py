# -*- coding: utf-8 -*-

#curl -X GET -H 'Content-type: application/json' https://anapioficeandfire.com/api/houses/378
import json
# import psycopg2 #not using switched to sqlite3 instead of setting up an external db for this example
import sqlite3

import requests

#run test for connection to db
def connect_to_db():
	db_connect = sqlite3.connect('test.db')

	db_cursor = db_connect.cursor()

	#db_cursor.execute('''CREATE TABLE boooks(name text, 
	#	                                     isbn text, 
	#	                                     publisher text, 
	#	                                     numberOfPages int, 
	#	                                     released date,
	#	                                     country text,
	#	                                     url text
	#	                                     mediaType text,
	#	                                     povCharacters text,
	#	                                     characters text,
	#	                                     authors text)''')
	
	#db_cursor.execute('''CREATE TABLE books(name text, 
	#	                                     isbn text, 
	#	                                     publisher text, 
	#	                                     numberOfPages int, 
	#	                                     country text)''')

	#db_cursor.execute("INSERT INTO books VALUES ('A Game of Thrones','978-0553103540','Bantam Books', 695, 'United States')")
	#db_connect.commit()

	for row in db_cursor.execute('SELECT * FROM books ORDER BY name'):
		print row

	db_connect.close()

	return("Wooooo DB Is working!")

def get_books():
	content = ''
	payload = {}
	book_data_attributes = []
	data_values = {}
	#sworn_members = []
	# Make a get request to get ONE BOOK
	response = requests.get("https://anapioficeandfire.com/api/books/1")
	#200, 301, 401, 400, 403, 404
	content = response.content

	payload = json.loads(response.content)
	#gets only keys for attribute name mapping 
	for i in payload:
		book_data_attributes.append(i)
	
	print( '--- --- ---')
	print( '--- --- ---')
	print( '--- BOOKS ---')	
	#print('DATA ATTRIBUTE NAMES:', book_data_attributes)

	#loads values
	for k, v in payload.iteritems():
		#loads data values
		#data_values.update(k,v)
		#if k == 'swornMembers':
		data_values.update({k:v})
		#    #gets sworn members
		#    if k == 'swornMembers' and v == '':
		#    	print('This House has no sworm members')
		#    else:
		#    	sworn_members.append(v)
	#print( '--- --- ---')
	#print( '--- --- ---')
	#print('SAMPLE VALUES:', data_values)

	#print( '--- --- ---')
	#print( '--- --- ---')
	#print( '--- --- ---')
	#print('SWORN MEMBERS:', sworn_members)
	return book_data_attributes


def get_characters():
	content = ''
	payload = {}
	character_data_attributes = []
	data_values = {}
	#sworn_members = []
	# Make a get request to get ONE CHARACTER
	response = requests.get("https://anapioficeandfire.com/api/characters/378")
	#200, 301, 401, 400, 403, 404
	content = response.content

	payload = json.loads(response.content)
	#gets only keys for attribute name mapping 
	for i in payload:
		character_data_attributes.append(i)

	print( '--- --- ---')
	print( '--- --- ---')
	print( '--- CHARACTERS ---')	
	#print('DATA ATTRIBUTE NAMES:', character_data_attributes)

	#loads values
	for k, v in payload.iteritems():
		#loads data values
		#data_values.update(k,v)
		#if k == 'swornMembers':
		data_values.update({k:v})
		#    #gets sworn members
		#    if k == 'swornMembers' and v == '':
		#    	print('This House has no sworm members')
		#    else:
		#    	sworn_members.append(v)
	#print( '--- --- ---')
	#print( '--- --- ---')
	#print('SAMPLE VALUES:', data_values)

	#print( '--- --- ---')
	#print( '--- --- ---')
	#print( '--- --- ---')
	#print('SWORN MEMBERS:', sworn_members)
	return character_data_attributes


def get_houses():
	content = ''
	payload = {}
	house_data_attributes = []
	data_values = {}
	sworn_members = []
	# Make a get request to get the ONE HOUSE.
	response = requests.get("https://anapioficeandfire.com/api/houses/378")
	#200, 301, 401, 400, 403, 404
	content = response.content

	payload = json.loads(response.content)
	#gets only keys for attribute name mapping 
	for i in payload:
		house_data_attributes.append(i)

	print( '--- --- ---')
	print( '--- --- ---')
	print( '--- HOUSES ---')	
	#print('DATA ATTRIBUTE NAMES:', house_data_attributes)

	#loads values
	for k, v in payload.iteritems():
		#loads data values
		#data_values.update(k,v)
		#if k == 'swornMembers':
		data_values.update({k:v})
		    #gets sworn members
		    #if k == 'swornMembers' and v == '':
		    #	print('This House has no sworm members')
		    #else:
		    #	sworn_members.append(v)

	#print( '--- --- ---')
	#print( '--- --- ---')
	#cprint('SAMPLE VALUES:', data_values)

	#print( '--- --- ---')
	#print( '--- --- ---')
	#print( '--- --- ---')
	#print('SWORN MEMBERS:', sworn_members)
	return house_data_attributes


#print(get_books())
#print(get_houses())
#print(get_characters())
print(connect_to_db())


	


