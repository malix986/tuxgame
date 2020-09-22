from google.cloud import bigquery

client = bigquery.Client()

# for row in results:
#     title = row['title']
#     unique_words = row['unique_words']
#     print(f'{title:<20} | {unique_words}')


def set_hint(hint,character_id):

   query = 'SELECT * FROM tuxgame.character_list)'

   # Execute the SQL command
   res = client.query(query)
   output = res.result()
   print(output)

set_hint('bravissimo',4)