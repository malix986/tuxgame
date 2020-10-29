from flask import Flask, render_template, request, session, jsonify
import setup
import mysql_functions
import random_character as rc
import numpy

#https://cloud.google.com/appengine/docs/standard/python3/setting-up-environment

app = Flask(__name__)
app.secret_key = "giontravolta"

random = numpy.random.rand()

@app.route('/', methods=['GET', 'POST'])
def index():
   session.clear()
   return render_template(
      'index.html'
      )

@app.route('/load_player', methods=['GET', 'POST'])
def load_player():
   session['player_stats'] = setup.set_player_stats()
   if request.form['user']:
      user = request.form['user']
      session['player_stats']['username'] = user 
   session['character_list'] = mysql_functions.get_character_list()
   session['ranking'] = mysql_functions.get_session_ranking()
   print('eureka')
   return render_template(
      'load_player.html'
      )

@app.route('/hint', methods=['GET', 'POST'])
def hint():
   try:
      len(session['player_stats'])
      print('eureka2')
   except:
      session['player_stats'] = setup.set_player_stats()
      if request.form['user']:
         user = request.form['user']
         session['player_stats']['username'] = user 
      session['character_list'] = mysql_functions.get_character_list()
      session['ranking'] = mysql_functions.get_session_ranking()
      print('aio')
   set_new_round()

   return render_template(
      'hint.html', 
      show = "",
      remaining = session['character_stats']['hint_total']-1,
      tot_hint = len(session['character_stats']['hint_list_complete']),
      share = 100,
      score = session['player_stats']['score'],
      potential_score = 100,
      user = session['player_stats']['username'],
      life = session['player_stats']['life']
      )


@app.route('/load_hint', methods=['POST'])
def load_hint():
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

   return jsonify('',render_template('show_hint.html',
      show = session['hint_stats']['hint'],
      remaining = session['hint_stats']['count']-1,
      tot_hint = len(session['character_stats']['hint_list_complete']),
      share = 100-session['hint_stats']['share'],
      score = session['player_stats']['score'],
      potential_score = session['hint_stats']['potential_score'],
      user = session['player_stats']['username'],
      life = session['player_stats']['life']      
      ))


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
      if life < 1:
         mysql_functions.set_match(session['player_stats'])
         ranking_all = session['ranking'] # mysql_functions.get_ranking(session['player_stats'])
         ranking = setup.get_ranking(ranking_all,session['player_stats'],7)
         results = []
         for row in ranking:
            results.append(dict(row))
         fieldnames = [key for key in results[0].keys()]

         return render_template(
         'ending.html',
         esito = esito,
         color = color,
         winfail = winfail,
         score = session['player_stats']['score'],
         life = session['player_stats']['life'],
         user = session['player_stats']['username'],
         results=results, 
         fieldnames=fieldnames,
         len = len
         )
      else:
         set_new_round()
         return render_template(
         'answer.html',
         esito = esito,
         color = color,
         winfail = winfail,
         score = session['player_stats']['score'],
         life = session['player_stats']['life'],
         user = session['player_stats']['username']
         )

@app.route('/admin', methods=['GET', 'POST'])
def admin():
   character_name = session['character_stats']['name']
   all_hints = mysql_functions.get_character_hint_all(character_name)
   results = []
   for row in all_hints:
      results.append(dict(row))
   fieldnames = [key for key in results[0].keys()]

   return render_template(
      'admin.html', 
      results=results, 
      fieldnames=fieldnames,
      len = len,
      character_name = character_name
      )


@app.route('/admin_change', methods=['GET', 'POST'])
def admin_change():
   if request.method == 'POST':
      hint = request.form['hint']
      hint_raw = request.form['hint_id']
      is_active = request.form['is_active']
      character_name = session['character_stats']['name']

      sql = mysql_functions.update_hint_description(character_name, hint, hint_raw, is_active)
      all_hints = mysql_functions.get_character_hint_all(character_name)

      results = []
      for row in all_hints:
         results.append(dict(row))
      fieldnames = [key for key in results[0].keys()]
      return render_template(
         'admin.html', 
         results=results, 
         fieldnames=fieldnames,
         len = len,
         sql = sql
         )


@app.route('/admin_refresh', methods=['GET', 'POST'])
def admin_refresh():
      character_name = session['character_stats']['name']
      all_hints = mysql_functions.get_character_hint_all(character_name)

      results = []
      for row in all_hints:
         results.append(dict(row))
      fieldnames = [key for key in results[0].keys()]
      return render_template(
         'admin.html', 
         results=results, 
         fieldnames=fieldnames,
         len = len
         )

@app.route('/html5template', methods=['GET', 'POST'])
def html5template():
      
      return render_template(
         'html5template.html'
         )

@app.route('/hint_dummy', methods=['GET', 'POST'])
def hint_dummy():
      
      return render_template(
         'hint_dummy.html'
         ) 

@app.route('/answer_dummy', methods=['GET', 'POST'])
def answer_dummy():
      
      return render_template(
         'answer_dummy.html'
         ) 

def set_new_round():
   random_character = rc.get_random_character(session['character_list'])
   session['character_list'].remove(random_character)
   session['character_stats'] = setup.set_character_stats(random_character)


if __name__ == '__main__':
   app.run(debug = True)   