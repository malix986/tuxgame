from google.cloud import bigquery

client = bigquery.Client()

# for row in results:
#     title = row['title']
#     unique_words = row['unique_words']
#     print(f'{title:<20} | {unique_words}')


def set_hint(hint,character_id):

   query = 'INSERT INTO tuxgame.hint_list(character_id,hint) VALUES (' + str(character_id) + ',"' + str(hint) + '")'
   print('New entry.....')
   # Execute the SQL command
   client.query(query)
   print('New entry.....OK',end='\r')

set_hint('bravissimo',4)