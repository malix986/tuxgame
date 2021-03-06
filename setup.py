import random_character as rc
import random
import main
import time
import datetime

def set_player_stats():
    self = set_player_stats
    print(self.__name__ +'...')
    player_stats = {
        'score': 0,
        'life': 2,
        'username':'utente',
        'timestamp':datetime.datetime.fromtimestamp(time.time()).isoformat()
    }
    print(self.__name__ +' ok\n')
    return player_stats


def set_character_stats(char_to_guess):
    self = set_character_stats
    print(self.__name__ +'...')
    char_name = char_to_guess['name']
    hint_list_full = rc.get_character_hints(char_name)
    hint_list_complete = []
    for i in hint_list_full:
        random_hint_chunked = random.choice(i)
        hint_list_complete.append(random_hint_chunked)
    hint_list_complete = list(hint_list_complete)
    remaining_hints = hint_list_complete
    hint_total = len(hint_list_complete)

    character_stats = {
        'name': char_name,
        'hint_list_complete': hint_list_complete,
        'remaining_hints': remaining_hints,
        'hint_total': hint_total
    }
    print(self.__name__ +' ok')
    print('_____total chunks: ' + str(len(hint_list_complete)) + "\n")
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


def get_ranking(ranking,user,results):
    
    player_stats = {
        'data': 'TODAY',
        'punteggio': user['score'],
        'rank':'YOU ARE HERE',
        'username':user['username']
    }

    useful_rank = [] 
    top_list = []
    bottom_list = []
    for entry in ranking:
        if entry['punteggio'] >= player_stats['punteggio']:
            top_list.append(entry)
        if entry['punteggio'] < player_stats['punteggio']:
            entry['rank'] = entry['rank']+1
            bottom_list.append(entry)
    for limited in top_list[-results:]:
        useful_rank.append(limited)
    useful_rank.append(player_stats)
    for limited in bottom_list[:results]:
        useful_rank.append(limited)

    return useful_rank

