from flask import Flask, render_template, request
import setup
import mysql_functions

#https://cloud.google.com/appengine/docs/standard/python3/setting-up-environment

app = Flask(__name__)
app.config['ENV'] = 'development'

player_stats = {}
character_stats = {}
hint_stats = {}

@app.route('/', methods=['GET', 'POST'])
def index():
   global player_stats
   global character_stats

   player_stats = setup.set_player_stats()
   character_stats = setup.set_character_stats()

   return render_template(
      'index.html'
      )

@app.route('/hint', methods=['GET', 'POST'])
def hint():
   global hint_stats
   global character_stats
   global player_stats
   
   print(player_stats)
   user = player_stats['username']
   if request.form.get('user'):
      user = request.form.get('user')
      player_stats['username'] = user
   print('user ' + user + ' set')

   print('getting random hint')
   hint_stats = setup.get_random_hint(character_stats)
   setup.remove_used_hint(character_stats,hint_stats)
   mysql_functions.update_hint_shown(character_stats['name'], hint_stats['hint'], hint_stats['shown']+1)
   print('times shown: '+str(hint_stats['shown']))

   return render_template(
      'hint.html', 
      show = hint_stats['hint'],
      remaining = hint_stats['count']-1,
      tot_hint = len(character_stats['hint_list_complete']),
      share = hint_stats['share'],
      score = player_stats['score'],
      potential_score = hint_stats['potential_score'],
      user = user,
      life = player_stats['life']
      )

@app.route('/answer', methods=['GET', 'POST'])
def answer():
   global hint_stats
   global character_stats
   global player_stats

   print(player_stats)

   user = player_stats['username']
   score = player_stats['score']
   life = player_stats['life']
   if request.method == 'POST':
      answer = request.form['answer']
      l_answer = str(answer).lower()
      char_name = str(character_stats['name']).lower()
      if l_answer == char_name:
         color = '#d4edda'
         winfail = 'COMPLIMENTI!'
         esito = '...era proprio '+character_stats['name']
         print(hint_stats)
         mysql_functions.update_hint_guessed(character_stats['name'], hint_stats['hint'],hint_stats['guessed']+1)
         player_stats['score'] = setup.update_score(player_stats,hint_stats)
      else:
         color = '#f8d7da'
         winfail = 'PECCATO!'
         esito = 'Mi dispiace, hai risposto '+ answer + ', mentre la risposta corretta era '+ character_stats['name']
         print(hint_stats)
         mysql_functions.update_hint_wrong(character_stats['name'], hint_stats['hint'],hint_stats['wrong']+1)
         player_stats['life'] = setup.life_loss(player_stats)
         
      #carica già personaggio successivo
      life = player_stats['life']
      character_stats = setup.set_character_stats()
      if life < 1:
         mysql_functions.set_match(player_stats)
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
   