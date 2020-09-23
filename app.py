from flask import Flask, render_template, request
import setup
import mysql_functions

#https://cloud.google.com/appengine/docs/standard/python3/setting-up-environment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   setup.new_game()
   return render_template(
      'index.html',
      spoiler = setup.character_stats['name']
      )

@app.route('/hint', methods=['GET', 'POST'])
def hint():
   global potential_score
   
   user = setup.player_stats['username']
   if request.form.get('user'):
      user = request.form.get('user')
      setup.player_stats['username'] = user

   setup.get_random_hint()
   print('DEBUGGGGG')
   print(setup.character_stats['name'])
   print(setup.hint_stats['hint'])
   print(setup.hint_stats['shown'])   
   mysql_functions.update_hint_shown(setup.character_stats['name'], setup.hint_stats['hint'], setup.hint_stats['shown']+1)
   share = setup.hint_stats['share']
   potential_score = setup.hint_stats['potential_score']
   score = setup.player_stats['score']
   life = setup.player_stats['life']
   print('times shown: '+str(setup.hint_stats['shown']))
   return render_template(
      'hint.html', 
      show = setup.hint_stats['hint'],
      remaining = setup.hint_stats['count']-1,
      tot_hint = len(setup.character_stats['hint_list_complete']),
      share = share,
      score = score,
      potential_score = potential_score,
      user = user,
      life = life
      )

@app.route('/answer', methods=['GET', 'POST'])
def answer():
   user = setup.player_stats['username']
   score = setup.player_stats['score']
   life = setup.player_stats['life']
   if request.method == 'POST':
      answer = request.form['answer']
      l_answer = str(answer).lower()
      char_name = str(setup.character_stats['name']).lower()
      if l_answer == char_name:
         color = '#d4edda'
         winfail = 'COMPLIMENTI!'
         esito = '...era proprio '+setup.character_stats['name']
         mysql_functions.update_hint_guessed(setup.hint_stats['hint'],setup.hint_stats['guessed']+1)
         setup.update_score()
      else:
         color = '#f8d7da'
         winfail = 'PECCATO!'
         esito = 'Mi dispiace, hai risposto '+ answer + ', mentre la risposta corretta era '+ setup.character_stats['name']
         mysql_functions.update_hint_wrong(setup.hint_stats['hint'],setup.hint_stats['wrong']+1)
         setup.life_loss()
      #carica già round successivo
      
      setup.new_round()
      if life == 0:
         mysql_functions.set_match()
         return render_template(
         'ending.html',
         esito = esito,
         color = color,
         winfail = winfail,
         score = score,
         life = life,
         user = user
         )
      else:
         return render_template(
         'answer.html',
         esito = esito,
         color = color,
         winfail = winfail,
         score = score,
         life = life,
         user = user
         )


if __name__ == '__main__':
   app.run(debug = True)
   