# python3 -m pip install --upgrade pymysql
# https://www.db4free.net/about.php
import pymysql
import time
import settings
import setup

settings.init()

def set_character_name(character_name):
   db = settings.db
   cursor = settings.cursor
   ## Prepare SQL query to INSERT the new record into the database.
   print('  Setting character entry for: '+character_name)
   sql = 'INSERT INTO character_list(name) VALUES ("' + str(character_name) + '")'
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print(character_name + ' insert in character_list correctly \n')

def get_character_id(character_name):
   cursor = settings.cursor
   sql = 'SELECT id FROM character_list WHERE name = "' + str(character_name) + '"'
   print('  getting character id')
   # Execute the SQL command
   cursor.execute(sql)
   print('SQL executed')
   # Fetch all the rows in a list of lists.
   row = cursor.fetchone()
   print('character_id: '+str(row[0])+'\n')
   character_id = row[0]
   return character_id

def set_hint(hint,character_id):
   db = settings.db
   cursor = settings.cursor   
   print('New entry.....')
   sql = 'INSERT INTO hint_list(character_id,hint) VALUES (' + str(character_id) + ',"' + str(hint) + '")'
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print('New entry.....OK',end='\r')

def get_hint(hint_id):
   sql = "SELECT * FROM hint_list WHERE id = " + str(hint_id)
   array_list = query_to_array(sql)
   return array_list

def get_character_list():
   sql = "SELECT * FROM character_list"
   array_list = query_to_array(sql)
   return array_list

def get_character_hint(character_id):
   sql = "SELECT * FROM hint_list WHERE character_id = " + str(character_id)
   array_list = query_to_array(sql)
   return array_list

def query_to_array(sql):
   cursor = settings.cursor
   cursor.execute(sql)
   return cursor.fetchall()

def update_hint_shown(hint_id, hint_shown):
   db = settings.db
   cursor = settings.cursor
   sql = "UPDATE hint_list SET shown = "+str(hint_shown)+" WHERE id ="+str(hint_id)
   cursor.execute(sql)
   db.commit()

def update_hint_guessed(hint_id, hint_guessed):
   db = settings.db
   cursor = settings.cursor
   sql = "UPDATE hint_list SET guessed = "+str(hint_guessed)+" WHERE id ="+str(hint_id)
   cursor.execute(sql)
   db.commit()

def update_hint_wrong(hint_id, hint_wrong):
   db = settings.db
   cursor = settings.cursor
   sql = "UPDATE hint_list SET wrong = "+str(hint_wrong)+" WHERE id ="+str(hint_id)
   cursor.execute(sql)
   db.commit()

def set_match():
   db = settings.db
   cursor = settings.cursor 
   user = str(setup.player_stats['username'])
   score = str(setup.player_stats['score'])

   print('New entry.....')
   sql = 'INSERT INTO session_list(username,score,date) VALUES ("' + user + '",' + score + ',CURRENT_TIMESTAMP)'
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()

# def get_ranking(user):
#    sql = """SELECT rank, username, score, DATE(date) FROM 
#       (SELECT username, score, DATE(date) RANK() OVER(ORDER BY score,date) FROM session_list
#       WHERE username = '""" + str(user) + """' ORDER BY score DESC"""
#    array_list = query_to_array(sql)
#    return array_list
