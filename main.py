from google.cloud import bigquery

client = bigquery.Client()

# for row in results:
#     title = row['title']
#     unique_words = row['unique_words']
#     print(f'{title:<20} | {unique_words}')

def get_character_id(character_name):
   sql = 'SELECT ROW_NUMBER() OVER() AS id FROM character_list WHERE name = "' + str(character_name) + '"'
   print('  getting character id')
   # Execute the SQL command
   results = client.query(query)
   print('SQL executed')
   # Fetch all the rows in a list of lists.
   
   print('character_id: '+str(result[0])+'\n')
   character_id = result[0]
   return character_id

print(get_character_id('lighter'))