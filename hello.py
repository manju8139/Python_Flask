from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to home page'

@app.route('/adminhome')
def admin():
    return 'welcome to admin home page'

@app.route('/userhome/<uname>')
def user(uname):
    return 'welcome %s to home page' % uname

@app.route('/checkauth/<uname>/<pword>')
def auth(uname,pword):
    if uname == 'admin' and pword == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('user',uname = uname))

if __name__ == '__main__':
    app.run(debug=True)
