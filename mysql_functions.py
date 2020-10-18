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
    sql = 'INSERT INTO tuxgame.hint_list(character_name,hint,hint_shown,hint_guessed,hint_wrong,hint_raw,is_active,id) VALUES ("' + str(character_name) + '","' + str(hint) + '",0,0,0,"' + str(hint) + '",True,CAST(FLOOR(1000000000*RAND()) AS INT64))'
    # Execute the SQL command
    client.query(sql)


def get_character_list():
    self = get_character_list
    print(self.__name__ +'...')
    sql = "SELECT * FROM tuxgame.character_list"
    results = client.query(sql)
    character_list = []
    for row in results:
        array_dict = {
            'name': row['name']
        }
        character_list.append(array_dict)
    print(self.__name__ +' ok\n')
    return character_list


def get_character_hint(character_name):
    self = get_character_hint
    print(self.__name__ +'...')
    sql = 'SELECT * FROM tuxgame.hint_list WHERE character_name = "' + str(character_name)+'" AND is_active = True'
    array_list = hint_query_to_array(sql, 10)
    print(self.__name__ +' ok\n')
    return array_list


def get_character_hint_all(character_name):
    sql = 'SELECT * FROM tuxgame.hint_list WHERE character_name = "' + str(character_name)+'"'
    array_list = query_to_array(sql)
    return array_list

def query_to_array(sql):
    results = client.query(sql)
    array_list = []
    for row in results:
        array_list.append(row)
    return array_list


def hint_query_to_array(sql, chunks):
    self = hint_query_to_array
    print(self.__name__ +'...')    
    results = client.query(sql)
    array_list = []
    for row in results:
        array_dict = {
            'character_name': row['character_name'],
            'hint': row['hint'],
            'hint_raw': row['hint_raw'],
            'hint_shown': row['hint_shown'],
            'hint_guessed': row['hint_guessed'],
            'hint_wrong': row['hint_wrong'],
            'easyness': row['hint_guessed']/row['hint_shown'] - row['hint_wrong']/row['hint_shown'] if row['hint_shown'] else 0
        }
        array_list.append(array_dict)
    sorted_array = sorted(array_list, key=lambda k: k['easyness'])
    step = math.floor(len(sorted_array)/chunks)
    print('Full Array of #' + str(len(sorted_array)) + ' hints divided in ' + str(chunks) + ' chunks of '+str(step))
    # Yields successive 'n' sized chunks from list 'list_name'
    for i in range(0, len(sorted_array), step):
        yield sorted_array[i:i + step]
    print(self.__name__ +' ok\n')
    return sorted_array


def update_hint_shown(character_name, hint, hint_shown):
    sql = 'UPDATE tuxgame.hint_list SET hint_shown = '+str(hint_shown)+' WHERE hint = "'+str(hint)+'" AND character_name ="'+str(character_name)+'"'
    client.query(sql)


def update_hint_guessed(character_name, hint, hint_guessed):
    sql = 'UPDATE tuxgame.hint_list SET hint_guessed = '+str(hint_guessed)+' WHERE hint = "'+str(hint)+'" AND character_name ="'+str(character_name)+'"'
    print(sql)
    client.query(sql)


def update_hint_wrong(character_name, hint, hint_wrong):
    sql = 'UPDATE tuxgame.hint_list SET hint_wrong = '+str(hint_wrong)+' WHERE hint = "'+str(hint)+'" AND character_name ="'+str(character_name)+'"'
    print(sql)
    client.query(sql)

def update_hint_description(character_name, hint, hint_id, is_active):
    sql = 'UPDATE tuxgame.hint_list SET hint = "'+str(hint)+'", is_active = '+str(is_active)+' WHERE id = '+str(hint_id)+' AND character_name ="'+str(character_name)+'"'
    print('UPDATE HINT: '+sql)
    client.query(sql)
    return sql

def set_match(player_stats):
    user = str(player_stats['username'])
    score = str(player_stats['score'])
    timestamp = str(player_stats['timestamp'])

    print('New entry.....')
    sql = 'INSERT INTO tuxgame.session_list(username,score,timestamp) VALUES ("' + user + '",' + score + ',"' + timestamp + '")'
    # Execute the SQL command
    client.query(sql)

def get_ranking(player_stats):
    user = str(player_stats['username'])
    score = str(player_stats['score'])
    timestamp = str(player_stats['timestamp'])
    sql = """
        SELECT
            RANK() OVER (ORDER BY score desc) AS rank,
            username,
            extract(date from timestamp) AS data,
            score AS punteggio
        FROM
            (SELECT
                username,
                score,
                timestamp
            FROM 
                tuxgame.session_list
            )
    """
    array_list = query_to_array(sql)
    print('user: ' +user+' score: '+score+' time: '+timestamp)
    return array_list