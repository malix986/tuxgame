import pymysql

import os

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

if os.environ.get('GAE_ENV') == 'standard':
    unix_socket = '/couldsql/{}'.format(db_connection_name)
    cnx = pymysql.connect(user=db_user, password=db_password, unix_socket=unix_socket, db=db_name)
else:
    host = '34.65.22.169'
    cnx = pymysql.connect(user=db_user, password=db_password, host=host, db=db_name)

with cnx.cursor() as cursor:
    cursor.execute('SELECT * FROM test_table')  #('insert into test_table(stringa) VALUES ("pluto")')
    result = cursor.fetchall()
    current_msg = result[0][0]
cnx.close()

print('hello works')
