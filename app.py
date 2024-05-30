from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_mysqldb import MySQL, MySQLdb
import re

import os
import main
import csv


app = Flask(__name__)

app.secret_key = "course_related_project1"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'timeslotdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
# Login & Register
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']  # Adjusted to match the assumed column name
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully!'
            return load_index()
        else:
            message = 'Please enter correct email / password!'
    return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            message = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address!'
        elif not userName or not password or not email:
            message = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s)', (userName, email, password,))
            mysql.connection.commit()
            message = 'You have successfully registered!'
    elif request.method == 'POST':
        message = 'Please fill out the form!'
    return render_template('register.html', message=message)


@app.route('/load')
def load_index():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM events ORDER BY id")
        calendar = cursor.fetchall()
        cursor.close()
        return render_template('index.html', calendar=calendar)
    return redirect(url_for('login'))

# Edit calendar
@app.route("/insert", methods=["POST"])
def insert():
    if request.method == 'POST':
        course = request.form['course']
        credits = request.form['credits']
        professor = request.form['professor']
        room = request.form['room']
        start = request.form['start']
        end = request.form['end']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO events (course, credits, professor, room, start, end) VALUES (%s, %s, %s, %s, %s, %s)", [course, credits, professor, room, start, end])
        mysql.connection.commit()
        cursor.close()

        msg = 'Added Successfully'
        return redirect(url_for('index'))

@app.route("/update", methods=["POST"])
def update():
    if request.method == 'POST':
        course = request.form['course']
        credits = request.form['credits']
        professor = request.form['professor']
        room = request.form['room']
        start = request.form['start']
        end = request.form['end']
        id = request.form['id']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE events SET course = %s, credits = %s profname = %s, class = %s, start = %s, end= %s WHERE id = %s", [course, credits, professor, room, start, end, id])
        mysql.connection.commit()
        cursor.close()

        msg = 'Updated Successfully'
        return jsonify(msg)

@app.route("/ajax_delete", methods=["POST"])
def ajax_delete():
    if request.method == 'POST':
        getid = request.form['id']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM events WHERE id = %s', [getid])
        mysql.connection.commit()
        cursor.close()

        msg = 'Record deleted successfully'
        return jsonify(msg)
    

# Generate Calendar
@app.route('/generate')
def generate():
    # Delete all records in the table
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM events')
    mysql.connection.commit()
    cursor.close()
    # Generate new calendar
    main.run()
    cwd = os.getcwd()
    path = os.path.join(cwd, 'database\output.csv')
    with open(path, 'r') as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
                if count == 0:
                    count+=1
                    continue
                course = row[1]
                credits = row[2]
                professor = row[3]
                room = row[4]
                start = row[5]
                end = row[6]
                
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute("INSERT INTO events (course, credits, professor, room, start, end) VALUES (%s, %s, %s, %s, %s, %s)", [course, credits, professor, room, start, end])
                mysql.connection.commit()
                cursor.close()

    msg = 'Added Successfully'
    return load_index()

if __name__ == "__main__":
    app.run(debug=True)
