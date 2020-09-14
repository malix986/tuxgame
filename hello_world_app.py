from flask import Flask, render_template, request
# import setup
# import mysql_functions

#https://cloud.google.com/appengine/docs/standard/python3/setting-up-environment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   setup.new_game()
   return render_template(
      'index.html',
      spoiler = 'pippo'
      )

@app.route('/hint', methods=['GET', 'POST'])
def hint():
   global potential_score
   
   user = 'username'

   share = 'share'
   potential_score = 'potential_score'
   score = 'score'
   life = 'life'
   print('hint id: 2')
   print('times shown: 3')
   return render_template(
      'hint.html', 
      show = 'hint',
      remaining = 'count',
      tot_hint = 'hint_list_complete',
      share = 4,
      score = 5,
      potential_score = potential_score,
      user = user,
      life = life
      )

@app.route('/answer', methods=['GET', 'POST'])
def answer():
   color = '#d4edda'
   winfail = 'COMPLIMENTI!'
   esito = '...era proprio stoca'
   return render_template(
   'ending.html',
   esito = esito,
   color = color,
   winfail = winfail,
   score = 4,
   life = 5,
   user = 'user'
   )

if __name__ == '__main__':
   app.run(debug = True)
   