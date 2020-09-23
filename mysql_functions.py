import time
import setup
from google.cloud import bigquery

## NEW CODE
client = bigquery.Client()

def set_character_name(character_name):
   ## Prepare SQL query to INSERT the new record into the database.
   sql = 'INSERT INTO tuxgame.character_list(name) VALUES ("' + str(character_name) + '")'
   # Execute the SQL command
   client.query(sql)
   print(character_name + ' insert in character_list correctly \n')

def set_hint(hint,character_name):
   sql = 'INSERT INTO tuxgame.hint_list(character_name,hint) VALUES ("' + str(character_name) + '","' + str(hint) + '")'
   # Execute the SQL command
   client.query(sql)

def get_character_list():
   sql = "SELECT * FROM tuxgame.character_list"
   array_list = query_to_array(sql)
   return array_list

def get_character_hint(character_name):
   sql = 'SELECT * FROM tuxgame.hint_list WHERE character_name = "' + str(character_name)+'"'
   array_list = query_to_array(sql)
   return array_list

def query_to_array(sql):
   results = client.query(sql)
   array_list = []
   for row in results:
       array_list.append(row)
   return array_list

def update_hint_shown(character_name, hint, hint_shown):
   sql = 'UPDATE tuxgame.hint_list SET hint_shown = '+str(hint_shown)+' WHERE hint = "'+str(hint)+'" AND character_name ="'+str(character_name)+'"'
   client.query(sql)

def update_hint_guessed(character_name, hint, hint_guessed):
   sql = 'UPDATE tuxgame.hint_list SET hint_guessed = '+str(hint_guessed)+' WHERE hint = "'+str(hint)+'" AND character_name ="'+str(character_name)+'"'
   client.query(sql)

def update_hint_wrong(character_name, hint, hint_wrong):
   sql = 'UPDATE tuxgame.hint_list SET hint_wrong = '+str(hint_wrong)+' WHERE hint = "'+str(hint)+'" AND character_name ="'+str(character_name)+'"'
   client.query(sql)

def set_match():
   user = str(setup.player_stats['username'])
   score = str(setup.player_stats['score'])

   print('New entry.....')
   sql = 'INSERT INTO tuxgame.session_list(username,score,timestamp) VALUES ("' + user + '",' + score + ',CURRENT_TIMESTAMP)'
   # Execute the SQL command
   client.query(sql)

## LEGACY CODE


# def get_ranking(user):
#    sql = """SELECT rank, username, score, DATE(date) FROM 
#       (SELECT username, score, DATE(date) RANK() OVER(ORDER BY score,date) FROM session_list
#       WHERE username = '""" + str(user) + """' ORDER BY score DESC"""
#    array_list = query_to_array(sql)
#    return array_list
