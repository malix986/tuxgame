import guess_character as guess
import random_character as rc
import random
import numpy
import mysql_functions
import time

# char_to_guess
# char_id
# char_name
# hint_list_complete
# remaining_hints

def new_round():
    global char_to_guess
    global char_id
    global char_name
    global hint_list_complete
    global remaining_hints

    char_to_guess = rc.get_random_character()
    char_id = char_to_guess[0]
    char_name = char_to_guess[1]
    hint_list_complete = rc.get_character_hints(char_id)
    hint_list_complete = list(hint_list_complete)
    remaining_hints = hint_list_complete

def get_random_hint():
    global random_hint
    global hint
    global hint_count
    global hint_id
    global hint_shown
    global hint_guessed
    global hint_wrong
    random_hint = random.choice(hint_list_complete)
    hint_id = random_hint[0]
    hint = random_hint[2]
    hint_shown = random_hint[3]
    hint_guessed = random_hint[4]
    hint_wrong = random_hint[5]

def print_hint():
    global hint
    global hint_count
    print(hint)
    print(str(hint_count-1)+' hints left')
    print('\n')

def next_hint():
    global remaining_hints
    global random_hint
    global hint_count
    global play

    if hint_count == 1:
        print('no more hints')
        play = False
    else:
        remaining_hints.remove(random_hint)
        get_random_hint()
        hint_count = len(remaining_hints)
        print(hint)
        print(str(hint_count-1)+' hints left')
        print('\n')

def move_scenario():
    global answer
    global char_name
    global play
    global hint
    global hint_shown
    global hint_guessed
    global hint_wrong
    global game

    if answer == 'next_hint':
        next_hint()
        hint_shown = hint_shown+1
        mysql_functions.update_hint_shown(hint_id,hint_shown)        
    elif answer == 'quit_game':
        print('Peccato... era '+char_name)
        play = False 

    elif answer == 'repeat':
        print('da capire')
        print_hint()
    else:
        if answer == char_name:
            print('GIUSTO!')
            hint_guessed = hint_guessed+1
            mysql_functions.update_hint_guessed(hint_id,hint_guessed)
            play = False
        else:
            print('sbagliato, era '+char_name)
            hint_wrong = hint_wrong+1
            mysql_functions.update_hint_wrong(hint_id,hint_wrong)
            play = False

def start_game():
    global game
    global hint_count
    global hint_shown
    global answer
    global play

    game = True

    while game == True:
        # load round
        new_round()
        get_random_hint()
        hint_count = len(remaining_hints)
        # start round
        print('Round starting in... 3',end='\r')
        time.sleep(1)
        print('Round starting in... 2',end='\r')
        time.sleep(1)
        print('Round starting in... 1',end='\r')
        time.sleep(1)
        print('NEW ROUND                    \n')

        # load hint
        play = True
        print_hint()
        hint_shown = hint_shown+1
        mysql_functions.update_hint_shown(hint_id,hint_shown)

        while play == True:
            answer = guess.move()
            move_scenario()

        game = guess.continue_game()

new_round()
print(len(remaining_hints))
# start_game()
# print('grazie! \n \n')
