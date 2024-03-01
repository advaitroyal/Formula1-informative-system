import profile
import sqlite3
from flask import Flask, render_template, request, url_for, flash
from cs50 import SQL
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__, template_folder='template')
db=SQL('sqlite:///TSPF.db')


@app.route('/',methods=['POST','GET'])
def homepage():
    return render_template('/homepage.html')

@app.route('/search',methods=['GET'])
def search():
    if request.method=='GET':
        record = db.execute("SELECT * FROM CONTENT where title='#(cs50 video)#'")
        return render_template('search.html')

@app.route('/moviepage1',methods=['GET'])
def moviepage1():
    if request.method=="GET":
        record = db.execute("SELECT * FROM CONTENT where Title ='Interstellar'")
        return render_template('moviepage1.html',record=record[0])


@app.route('/sub',methods=['GET'])
def subscription():
    if request.method=="GET":
        record = db.execute("SELECT * from Subscription")
        return render_template('sub.html')
    
@app.route('/payment',methods=['GET','POST'])
def payment():
    if request.method=="GET":
        record = db.execute("SELECT * from Payment")
        return render_template('payment.html')


@app.route('/viewprofile',methods=['POST','GET'])
def viewprofile():
    if request.method=="GET":
        
        record = db.execute("SELECT * FROM User where UID=1")
        return render_template('viewprofile.html',record=record[0])
    
@app.route('/updateprofile',methods=['POST','GET'])
def updateprofile():
    if request.method=="POST":
        Firstname=request.form["First name"]
        Lastname=request.form["Last name"]
        Emailid=request.form["Email id"]
        db.execute("UPDATE USER SET First_name=:Firstname,Last_name=:Lastname,Email_id=:Emailid WHERE UID=1",UID=int(
            Firstname=request.form["First name"],Lastname=request.form["Last name"],Emailid=request.form["Email id"]
        ))
        return render_template('updateprofile.html')
    else:   
        return render_template('updateprofile.html')

@app.route('/login_regis',methods=['POST','GET'])
def login_regis():
    if request.method=="POST":
        db.execute("INSERT INTO USER")
        render_template('login_regis.html')
        
@app.route('/movie')
def index():
    try:
        socks = db.execute("SELECT * from USER where Genre='Drama'")
        sock_text = '<ul>'
        for sock in socks:
            sock_text += '<li>' + db.Genre + ', ' + db.Title + '</li>'
        sock_text += '</ul>'
        return sock_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
        
if __name__=='__main__':
    app.run(debug=True)