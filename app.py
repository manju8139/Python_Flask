from flask import Flask, redirect, url_for,request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('adminhome.html')

@app.route('/home/<string:user>')
def hello1(user):
    return render_template('userhome.html',user=user)

@app.route('/usignup')
def signup():
    return render_template('userSignup.html')

@app.route('/usignupcheck',methods = ['POST','GET'])
def signupcheck():
    if request.method == 'POST':
        data = request.form
        return render_template('userResult.html',result = data)
    else:
        return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    if(name == 'admin'):
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello1',user=name))
    
# HTTP Methods route for POST and GET
@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('user',name = user))

@app.route('/marks')
def marks():
    dict = {"P":100,"C":96,"M":100}
    return render_template('userMarks.html',marks = dict)

if __name__ == '__main__':
    app.run(debug = True)