import mysql_functions as ms
import random


# GET ID AND NAME OF RANDOM CHARACTER
def get_random_character(character_list):
    self = get_random_character
    print(self.__name__ +'...',end='\r')
    random_character = random.choice(character_list)
    print(self.__name__ +' ok\n')
    return random_character


# GET HINTS RELATED TO DEFINED CHARACTER
def get_character_hints(char_name):
    hint_list = ms.get_character_hint(char_name)
    return hint_list
