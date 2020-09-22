from google.cloud import bigquery

client = bigquery.Client()

# for row in results:
#     title = row['title']
#     unique_words = row['unique_words']
#     print(f'{title:<20} | {unique_words}')

def set_character_name(character_name):
   ## Prepare SQL query to INSERT the new record into the database.
   query = 'INSERT INTO character_list(name) VALUES ("' + str(character_name) + '")'
   # Execute the SQL command
   results = client.query(query)
   print(character_name + ' insert in character_list correctly \n')

set_character_name('fortunadia')