from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'path/to/file.json')

project_id = 'my-bq'
client = bigquery.Client(credentials= credentials,project=project_id)

def get_character_hint(character_id):
   sql = "SELECT * FROM (SELECT * FROM (SELECT *, ROW_NUMBER() OVER() AS id FROM tuxgame.hint_list) WHERE character_id = " + str(character_id)+")"
   array_list = query_to_array(sql)
   return array_list

def query_to_array(sql):
   results = client.query(sql)
   array_list = []
   for row in results:
       array_list.append(row)
   return array_list

print(get_character_hint(6))