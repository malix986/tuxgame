import mysql_functions
import wiki_data
import time

def create(character_name):
    mysql_functions.set_character_name(character_name)
    print(str(character_name) + ' inserted correctly... now populating hint list')
    populate_hint_list(character_name)

def populate_hint_list(character_name):
    ## Get Description and populate sql
    print('Populating hints for '+character_name)
    hint_list = wiki_data.get_wiki_hints(character_name)
    counter = 0
    for hint in hint_list:
        if hint is not ' ':
            mysql_functions.set_hint(hint,character_name)
            print('New entry.... - '+str(counter),end='\r')
            counter = counter+1
    print(str(counter)+' new hints added!')
    # disconnect from server

character_list = ["Donatella Rettore","Renato Zero","Silvio Berlusconi","Paolo Bonolis","Fedez","Chiara Ferragni","Luciano Pavarotti","Pippo Baudo","Barbara D'Urso","Max Pezzali","Ambra Angiolini","Donald Trump","Topolino","Freddie Mercury","Emilio Fede"]

for char in character_list:
    create(char)

# "Renato Zero","Silvio Berlusconi","Paolo Bonolis","Fedez","Chiara Ferragni","Luciano Pavarotti","Pippo Baudo","Barbara D'Urso","Max Pezzali","Ambra Angiolini","Donald Trump","Topolino","Freddie Mercury","Emilio Fede"