from app import app
from flask_mysqldb import MySQL, MySQLdb

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'timeslotdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)