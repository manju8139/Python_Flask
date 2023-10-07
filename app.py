from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello manju,come to flask app'

@app.route('/admin')
def admin():
    return 'welcome to admin page'

@app.route('/home/<string:user>')
def hello1(user):
    return 'welcome %s' % user #or 'welcome' + name

@app.route('/user/<name>')
def user(name):
    if(name == 'admin'):
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello1',user=name))

        
if __name__ == '__main__':
    app.run(debug = True)