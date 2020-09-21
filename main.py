# This file contains all the code used in the codelab. 
import sqlalchemy

# Depending on which database you are using, you'll set some variables differently. 
# In this code we are inserting only one field with one value. 
# Feel free to change the insert statement as needed for your own table's requirements.

# Uncomment and set the following variables depending on your specific instance and database:
connection_name = "python-app-test-289520:europe-west6:wikigame"
table_name = "test_table"
table_field = "stringa"
table_field_value = "maronnasantissima"
db_name = "wikitest"
db_user = "root"
db_password = "IAmR00t"

# If your database is MySQL, uncomment the following two lines:
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

# If your database is PostgreSQL, uncomment the following two lines:
#driver_name = 'postgres+pg8000'
#query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})

# If the type of your table_field value is a string, surround it with double quotes.

def insert(request):
    request_json = request.get_json()
    stmt = sqlalchemy.text('insert into '+table_name+' ('+table_field+') values ("'+table_field_value+'")')
    
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'ok'