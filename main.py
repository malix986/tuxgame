from google.cloud import bigquery

client = bigquery.Client()

# for row in results:
#     title = row['title']
#     unique_words = row['unique_words']
#     print(f'{title:<20} | {unique_words}')

def get_hint(hint_id):
   sql = "SELECT * FROM (SELECT *, ROW_NUMBER() OVER() AS id FROM tuxgame.hint_list) WHERE id = " + str(hint_id)
   array_list = query_to_array(sql)
   return array_list

def query_to_array(sql):
   results = client.query(sql)
   array_list = []
   for row in results:
       array_list.append(row)
   return array_list

print(get_hint(2))