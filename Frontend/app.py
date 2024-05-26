from flask import Flask, render_template

#from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)


'''
app.secret_key = 'courserelatedproject1'

app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = '123456'
app.config['MySQL_DB'] = 'timeslotdb'
app.config['MySQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT * FROM events ORDER BY id')
    calendar = cur.fetchall()
    return render_template('index.html', calendar = calendar)

if __name__ == '__main__':
    app.run(debug = True)
'''
