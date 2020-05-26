import mysql_functions
import wiki_data
import time
import settings

settings.init()

db = settings.db
cursor = settings.cursor

def create(character_name):
    mysql_functions.set_character_name(character_name)
    character_id = mysql_functions.get_character_id(character_name)
    print(str(character_id) + ' char_id retrieved correctly')
    populate_hint_list(character_name,character_id)

def populate_hint_list(character_name,character_id):
    ## Get Description and populate sql
    print('Populating hints for '+character_name)
    hint_list = wiki_data.get_wiki_hints(character_name)
    counter = 0
    for hint in hint_list:
        if hint is not ' ':
            mysql_functions.set_hint(hint,character_id)
            counter = counter+1
    print(str(counter)+' new hints added!')
    # disconnect from server

character_list = ["Donatella Rettore"]

for char in character_list:
    create(char)

db.close()

# "Renato Zero","Silvio Berlusconi","Paolo Bonolis","Fedez","Chiara Ferragni","Luciano Pavarotti","Pippo Baudo","Barbara D'Urso","Max Pezzali","Ambra Angiolini","Donald Trump","Topolino","Freddie Mercury","Emilio Fede"