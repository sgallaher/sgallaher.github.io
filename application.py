import sqlite3
from flask import Flask,redirect,render_template, request, session
from flask_session import Session
from flask import jsonify
import os

def getApp():
    return app
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = os.getenv(db_file)
    except Error as e:
        print(e)

    return conn

def select_tasks(sql):

    db = create_connection("postgres://kkeecgtmrvdhhu:5c2c8cba3d13dc8a62bbb25913d6e10f1b620cb9bf258ceb1f4e45c965cea96a@ec2-54-74-14-109.eu-west-1.compute.amazonaws.com:5432/d1nfej218i2kg1")
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = db.cursor()
    cur.execute(sql)


    results = cur.fetchall()


    return results



app = Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)









@app.route("/", methods=["GET","POST"])
def index():
    sql=f'SELECT DISTINCT class FROM tblCharacters order by class;'
    classes = select_tasks(sql)
    print()
    if request.method == "POST":
        session["classcode"]=request.form.get("classcode")
        classcode=session['classcode']

    else:
        classcode=classes[0][0]

    sql=f'SELECT * FROM tblCharacters WHERE class="{classcode}" order by seat;'


    details = select_tasks(sql)

    return render_template("index.html", details=details, classes=classes)

'''
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method =="POST":
        # Remember that user logged in
        session["username"]=request.form.get("username")
        session["password"]=request.form.get("password")
        return redirect("/")
    return render_template("login.html")
'''
