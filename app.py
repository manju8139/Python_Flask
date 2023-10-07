from flask import Flask, redirect, url_for,request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello manju,come to flask app'

@app.route('/admin')
def admin():
    return render_template('adminhome.html')

@app.route('/home/<string:user>')
def hello1(user):
    return render_template('userhome.html',user=user)

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


if __name__ == '__main__':
    app.run(debug = True)