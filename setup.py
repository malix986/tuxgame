import random_character as rc
import random
import main

def set_player_stats():
    self = set_player_stats
    print(self.__name__ +'...',end='\r')
    player_stats = {
        'score': 0,
        'life': 2,
        'username':'utente'
    }
    print(self.__name__ +' ok\n')
    return player_stats


def set_character_stats():
    self = set_character_stats
    print(self.__name__ +'...',end='\r')
    char_to_guess = rc.get_random_character()
    char_name = char_to_guess['name']
    hint_list_full = rc.get_character_hints(char_name)
    hint_list_complete = []
    for i in hint_list_full:
        random_hint_chunked = random.choice(i)
        hint_list_complete.append(random_hint_chunked)
    hint_list_complete = list(hint_list_complete)
    remaining_hints = hint_list_complete
    hint_total = len(hint_list_complete)
    print('_____total chunks: ' + str(len(hint_list_complete)))

    character_stats = {
        'name': char_name,
        'hint_list_complete': hint_list_complete,
        'remaining_hints': remaining_hints,
        'hint_total': hint_total
    }
    print(self.__name__ +' ok \n')
    return character_stats


def get_random_hint(character_stats):
    self = get_random_hint
    print(self.__name__ +'...',end='\r')
    random_hint = character_stats['remaining_hints'][0]
    hint_count = len(character_stats['remaining_hints'])
    hint_total = character_stats['hint_total'] 
    hint_gone = hint_total - hint_count
    hint = random_hint['hint']
    hint_shown = random_hint['hint_shown']
    hint_guessed = random_hint['hint_guessed']
    hint_wrong = random_hint['hint_wrong']
    share = round(hint_gone/hint_total, 2)*100
    potential_score = round(100*(1-((hint_gone)/hint_total)))

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
    print(self.__name__ +' ok\n')
    return hint_stats


def remove_used_hint(character_stats,hint_stats):
    self = remove_used_hint
    print(self.__name__ +'...',end='\r')
    print(character_stats['remaining_hints'])
    if hint_stats['count'] > 1:
        character_stats['remaining_hints'].remove(hint_stats['random_hint'])
    elif hint_stats['count'] == 1:
        hint_stats['hint'] = hint_stats['hint']
    else:
        hint_stats['hint'] = 'INDIZI FINITI'
    print(character_stats['remaining_hints'])    
    print(self.__name__ +' ok\n')


def update_score(player_stats,hint_stats):
    self = update_score
    print(self.__name__ +'...',end='\r')
    player_stats['score'] = player_stats['score'] + hint_stats['potential_score']
    print(self.__name__ +' ok\n')
    return player_stats['score']


def life_loss(player_stats):
    self = life_loss
    print(self.__name__ +'...',end='\r')
    player_stats['life'] = player_stats['life'] - 1
    print(self.__name__ +' ok\n')
    return player_stats['life']

###################

# def new_game():    
#     global player_stats

#     print('\n \n ######## SETUP NEW GAME ########')
#     player_stats = {
#         'score': 0,
#         'life': 2,
#         'username':'utente'
#     }
#     new_round()


# def new_round():
#     global character_stats

#     print('\n \n ######## SETUP NEW ROUND ########')
#     char_to_guess = rc.get_random_character()
#     char_name = char_to_guess['name']
#     hint_list_full = rc.get_character_hints(char_name)
#     hint_list_complete = []
#     for i in hint_list_full:
#         random_hint_chunked = random.choice(i)
#         hint_list_complete.append(random_hint_chunked)
#     hint_list_complete = list(hint_list_complete)
#     remaining_hints = hint_list_complete
#     hint_total = len(hint_list_complete)
#     print('######## HINT LIST COMPLETE ########')
#     print(hint_list_complete)
#     print('_____total chunks: ' + str(len(hint_list_complete)))

#     character_stats = {
#         'char_to_guess': char_to_guess,
#         'name': char_name,
#         'hint_list_complete': hint_list_complete,
#         'remaining_hints': remaining_hints,
#         'hint_total': hint_total
#     }
#     print('######## DEBUG CHAR STATS IN setup.new_round ########')
#     print('character_stats len: ' + str(len(character_stats)))


# def old_get_random_hint():
#     global hint_stats
#     global character_stats

#     if character_stats == {}:
#         print('_____mannaggia, riprovo')
#         new_round()
#         print('riproviamo con '+ character_stats['name'])

#     # random_hint = random.choice(character_stats['remaining_hints'])
#     print('########## EXPECTED #########')
#     print(character_stats)

#     random_hint = character_stats['remaining_hints'][0]
#     hint_count = len(character_stats['remaining_hints'])
#     hint_total = character_stats['hint_total'] 
#     hint_gone = hint_total - hint_count +1
#     hint = random_hint['hint']
#     hint_shown = random_hint['hint_shown']
#     hint_guessed = random_hint['hint_guessed']
#     hint_wrong = random_hint['hint_wrong']
#     share = round(hint_gone/hint_total, 2)*100
#     potential_score = round(100*(1-((hint_gone-1)/hint_total)))

#     if hint_count > 1:
#         character_stats['remaining_hints'].remove(random_hint)
#     elif hint_count == 1:
#         hint = hint
#     else:
#         hint = 'INDIZI FINITI'

#     hint_stats = {
#         'random_hint': random_hint,
#         'count': hint_count,
#         'gone': hint_gone,
#         'hint': hint,
#         'shown': hint_shown,
#         'guessed': hint_guessed,
#         'wrong': hint_wrong,
#         'share': share,
#         'potential_score': potential_score
#     }
#     print('########## HINT STATS #########')
#     print(hint_stats)
#     print('########## EXPECTED #########')
#     print(character_stats)


# def old_update_score():
#     global player_stats
#     global hint_stats
#     player_stats['score'] = player_stats['score'] + hint_stats['potential_score']


# def old_life_loss():
#     global player_stats
#     player_stats['life'] = player_stats['life'] - 1


# #new_round()
# #print(character_stats['hint_list_complete'])
