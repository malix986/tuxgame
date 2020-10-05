from flask import Flask, render_template, request, session
import setup
import mysql_functions

#https://cloud.google.com/appengine/docs/standard/python3/setting-up-environment

app = Flask(__name__)
#SESSION_TYPE = 'filesystem'
app.secret_key = "giontravolta"
#app.config['ENV'] = 'development'

@app.route('/', methods=['GET', 'POST'])
def index():
   session.clear()

   session['player_stats'] = setup.set_player_stats()   
   session['character_stats'] = setup.set_character_stats()

   return render_template(
      'index.html'
      )

@app.route('/hint', methods=['GET', 'POST'])
def hint():
   user = session['player_stats']['username']
   if request.form.get('user'):
      user = request.form.get('user')
      session['player_stats']['username'] = user
   print('user ' + user + ' set')

   print('getting random hint')
   session['hint_stats'] = setup.get_random_hint(session['character_stats'])
   print(session['hint_stats'])
   print('remaining hints before')
   print(session['character_stats']['remaining_hints'])
   setup.remove_used_hint(session['character_stats'],session['hint_stats'])
   print('remaining hints after')
   print(session['character_stats']['remaining_hints'])
   mysql_functions.update_hint_shown(session['character_stats']['name'], session['hint_stats']['hint'], session['hint_stats']['shown']+1)
   print('times shown: '+str(session['hint_stats']['shown']))

   return render_template(
      'hint.html', 
      show = session['hint_stats']['hint'],
      remaining = session['hint_stats']['count']-1,
      tot_hint = len(session['character_stats']['hint_list_complete']),
      share = session['hint_stats']['share'],
      score = session['player_stats']['score'],
      potential_score = session['hint_stats']['potential_score'],
      user = session['player_stats']['username'],
      life = session['player_stats']['life']
      )

@app.route('/answer', methods=['GET', 'POST'])
def answer():
   if request.method == 'POST':
      answer = request.form['answer']
      l_answer = str(answer).lower()
      char_name = str(session['character_stats']['name']).lower()
      if l_answer == char_name:
         color = '#d4edda'
         winfail = 'COMPLIMENTI!'
         esito = '...era proprio '+session['character_stats']['name']
         print(session['hint_stats'])
         mysql_functions.update_hint_guessed(session['character_stats']['name'], session['hint_stats']['hint'],session['hint_stats']['guessed']+1)
         print('score prima')
         print(session['player_stats']['score'])
         session['player_stats']['score'] = setup.update_score(session['player_stats'],session['hint_stats'])
         print('score dopo')
         print(session['player_stats']['score'])
      else:
         color = '#f8d7da'
         winfail = 'PECCATO!'
         esito = 'Mi dispiace, hai risposto '+ answer + ', mentre la risposta corretta era '+ session['character_stats']['name']
         print(session['hint_stats'])
         mysql_functions.update_hint_wrong(session['character_stats']['name'], session['hint_stats']['hint'],session['hint_stats']['wrong']+1)
         session['player_stats']['life'] = setup.life_loss(session['player_stats'])
         
      #carica già personaggio successivo
      life = session['player_stats']['life']
      session['character_stats'] = setup.set_character_stats()
      if life < 1:
         mysql_functions.set_match(session['player_stats'])
         return render_template(
         'ending.html',
         esito = esito,
         color = color,
         winfail = winfail,
         score = session['player_stats']['score'],
         life = session['player_stats']['life'],
         user = session['player_stats']['username']
         )
      else:
         return render_template(
         'answer.html',
         esito = esito,
         color = color,
         winfail = winfail,
         score = session['player_stats']['score'],
         life = session['player_stats']['life'],
         user = session['player_stats']['username']
         )


if __name__ == '__main__':
   app.run(debug = True)   