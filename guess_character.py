def move():
    guess = input('Vuoi un altro indizio? (Y/N) \n')
    answered = answer(guess)
    return answered


def answer(choice):
    check_choice = str(choice).lower()
    if check_choice == 'y':
        return 'next_hint'
    elif check_choice == 'n':
        return 'quit_game'
    else:
        confirmation = confirm_name(choice)
        return confirmation


def continue_game():
    continue_game = input('Premi Q per uscire, o qualsiasi tasto per giocare ancora \n')
    continue_game = str(continue_game).lower()
    if continue_game == 'q':
        return False
    else: 
        return True


def confirm_name(choice):
    confirmation = input('Hai detto '+choice+', sei sicuro? (Y/N)')
    print(confirmation)
    if str(confirmation).lower() == 'y':
        return choice
    elif str(confirmation).lower() == 'n':
        print('Non Più sicuro - Ripeti la scelta')
        return 'repeat'
    else:
        print('Non Più sicuro - Ripeti la scelta e premi Y per confermare')
        return 'repeat'