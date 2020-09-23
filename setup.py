import guess_character as guess
import random_character as rc
import random
import numpy
import mysql_functions
import time


player_stats = {}
character_stats = {}
hint_stats = {}

def new_game():
    global player_stats
    player_stats = {
        'score': 0,
        'life': 2,
        'username':'utente'
    }
    new_round()

def new_round():
    global character_stats

    char_to_guess = rc.get_random_character()
    char_name = char_to_guess['name']
    hint_list_complete = rc.get_character_hints(char_name)
    hint_list_complete = list(hint_list_complete)
    print('HINTLISTCOMPLETE')
    print(hint_list_complete)
    remaining_hints = hint_list_complete
    hint_total = len(hint_list_complete)

    character_stats = {
        'char_to_guess': char_to_guess,
        'name': char_name,
        'hint_list_complete': hint_list_complete,
        'remaining_hints': remaining_hints,
        'hint_total': hint_total
    }

def get_random_hint():
    global hint_stats
    global character_stats

    random_hint = random.choice(character_stats['remaining_hints'])
    hint_count = len(character_stats['remaining_hints'])
    hint_gone = character_stats['hint_total'] - hint_count +1
    hint = random_hint['hint']
    hint_shown = random_hint['hint_shown']
    hint_guessed = random_hint['hint_guessed']
    hint_wrong = random_hint['hint_wrong']
    share = round(hint_gone/character_stats['hint_total'],2)*100
    potential_score = round(100*(1-((hint_gone-1)/character_stats['hint_total'])))

    if hint_count > 1:
        character_stats['remaining_hints'].remove(random_hint)
    elif hint_count == 1:
        hint = hint
    else:
        hint = 'INDIZI FINITI'  
    
    hint_stats = {
        'random_hint': random_hint,
        'count': hint_count,
        'gone': hint_gone,
        'hint': hint,
        'shown': hint_shown,
        'guessed': hint_guessed,
        'wrong': hint_wrong,
        'share': share,
        'potential_score': potential_score        
    }

def update_score():
    global player_stats
    global hint_stats
    player_stats['score'] = player_stats['score'] + hint_stats['potential_score']

def life_loss():
    global player_stats
    player_stats['life'] = player_stats['life'] -1