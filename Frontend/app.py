from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL,MySQLdb
 
app = Flask(__name__)
         
app.secret_key = "course_related_project1"
         
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'timeslotdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app) 
 
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM events ORDER BY id")
    calendar = cur.fetchall()  
    return render_template('index.html', calendar = calendar)
 
@app.route("/insert",methods=["POST","GET"])
def insert():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        print(title)     
        print(start)  
        cur.execute("INSERT INTO events (title,start_event,end_event) VALUES (%s,%s,%s)",[title,start,end])
        mysql.connection.commit()       
        cur.close()
        msg = 'success'  
    return jsonify(msg)
 
@app.route("/update",methods=["POST","GET"])
def update():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        id = request.form['id']
        print(title)     
        print(start)  
        cur.execute("UPDATE events SET title = %s, start_event = %s, end_event = %s WHERE id = %s ", [title, start, end, id])
        mysql.connection.commit()       
        cur.close()
        msg = 'success'  
    return jsonify(msg)    
 
@app.route("/ajax_delete",methods=["POST","GET"])
def ajax_delete():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['id']
        print(getid)
        cur.execute('DELETE FROM events WHERE id = {0}'.format(getid))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'  
    return jsonify(msg) 
 
if __name__ == "__main__":
    app.run(debug=True)