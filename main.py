import sqlite3
from flask import Flask,redirect,render_template, request, session
from flask_session import Session
from flask import jsonify


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_tasks(sql):

    db = create_connection("hp.db")
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
