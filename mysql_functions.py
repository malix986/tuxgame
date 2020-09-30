import time
import setup
import math

from google.cloud import bigquery

client = bigquery.Client()

def set_character_name(character_name):
    ## Prepare SQL query to INSERT the new record into the database.
    sql = 'INSERT INTO tuxgame.character_list(name) VALUES ("' + str(character_name) + '")'
    # Execute the SQL command
    client.query(sql)


def set_hint(hint, character_name):
    sql = 'INSERT INTO tuxgame.hint_list(character_name,hint,hint_shown,hint_guessed,hint_wrong) VALUES ("' + str(character_name) + '","' + str(hint) + '",0,0,0)'
    # Execute the SQL command
    client.query(sql)


def get_character_list():
    sql = "SELECT * FROM tuxgame.character_list"
    array_list = query_to_array(sql)
    return array_list


def get_character_hint(character_name):
    sql = 'SELECT * FROM tuxgame.hint_list WHERE character_name = "' + str(character_name)+'"'
    array_list = hint_query_to_array(sql, 10)
    return array_list


def query_to_array(sql):
    results = client.query(sql)
    array_list = []
    for row in results:
        array_list.append(row)
    return array_list


def hint_query_to_array(sql, chunks):
    results = client.query(sql)
    array_list = []
    for row in results:
        array_dict = {
            'character_name': row['character_name'],
            'hint': row['hint'],
            'hint_shown': row['hint_shown'],
            'hint_guessed': row['hint_guessed'],
            'hint_wrong': row['hint_wrong'],
            'easyness': row['hint_guessed']/row['hint_shown'] - row['hint_wrong']/row['hint_shown'] if row['hint_shown'] else 0
        }
        array_list.append(array_dict)
    sorted_array = sorted(array_list, key=lambda k: k['easyness'])
    step = math.ceil(len(sorted_array)/chunks)
    # Yields successive 'n' sized chunks from list 'list_name'
    for i in range(0, len(sorted_array), step):
        yield sorted_array[i:i + step]
    return sorted_array


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
