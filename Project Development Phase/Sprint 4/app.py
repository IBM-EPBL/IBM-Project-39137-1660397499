from flask import Flask,render_template, request, url_for, flash, redirect
import ibm_db
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('main.html')
@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        options = { ibm_db.SQL_ATTR_AUTOCOMMIT:  ibm_db.SQL_AUTOCOMMIT_ON }
        conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30120;PROTOCOL=TCPIP;UID=qps31941;PWD=80vvdGf8o1OrRKD4",'','', options)

        sql = "SELECT * FROM students WHERE name =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,name)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            return render_template('main.html', msg="You are already a member, please login using your details")
        else:
            insert_sql = "INSERT INTO User_data VALUES (?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)

            ibm_db.execute(prep_stmt)
        
        return render_template('main.html', msg="Data saved successfuly..")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/forgot")
def forgot():
    return render_template('forgot.html')

@app.route("/dashboard")
def dashbord():
    return render_template('dashboard.html')

@app.route("/wallet")
def wallet():
    return render_template('wallet.html')

@app.route("/expenses")
def expenses():
    return render_template('expenses.html')

@app.route("/email")
def email():
    return render_template('email.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5000,debug=True)