
from flask import Flask, redirect,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['uname']
        password = request.form['psw']
        return render_template('main.html')
    if request.method=='GET':
        return render_template('login.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        username = request.form['uname']
        password = request.form['Psw']
        email = request.form['email']
        return render_template('main.html')
    if request.method=='GET':
        return render_template('signup.html')



if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5000,debug=True)
