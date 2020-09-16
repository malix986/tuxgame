import mysql_functions
import settings

print('hello works')

settings.init()

db = settings.db
cursor = settings.cursor
## Prepare SQL query to INSERT the new record into the database.
print('cursor set')
sql = 'insert into test_table(stringa) VALUES ("pluto")'
# Execute the SQL command
cursor.execute(sql)
print('cursor executed')
# Commit your changes in the database
db.commit()
print('cursor committed \n')
