import mysql_functions as ms
import random

#GET ID AND NAME OF RANDOM CHARACTER
def get_random_character():
    all_character_array = ms.get_character_list()
    random_character = random.choice(all_character_array)
    return random_character

#GET HINTS RELATED TO RANDOM CHARACTER
def get_random_character_hints():
    random_character = get_random_character()
    hint_list = ms.get_character_hint(random_character[0])
    return hint_list

#GET HINTS RELATED TO RANDOM CHARACTER
def get_character_hints(character_id):
    hint_list = ms.get_character_hint(character_id)
    return hint_list

