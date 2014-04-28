from flask import Flask
from flask import request
from flask import render_template, url_for
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test2.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        myusers = 'User: %r' % self.username+ ', email: %r' % self.email
        myusers = str(myusers)
        myusers = myusers.replace(" u'", " ").replace("'", "")
        return myusers
        
# searchword = request.args.get('course', '')
@app.route('/')
def hello_world():
    return 'Hello Jose Vieitez - Rapid Prototyping 2014!'

@app.route('/find')
def hello():
	searchword = request.args.get('course', '')
	error = None
	if searchword == 'CSCI1300':
		return 'Find the classroom for '+searchword+'...   ATLAS 100'
	if searchword == 'CSCI2240':
		return 'Find the classroom for '+searchword+'...   ITTL 1B50'
	else: 
		error = 'no result'
	return 'Find the classroom for '+searchword+'... Sorry No results for  '+searchword



@app.route('/notification')
def notification():
	return 'Get notification. To be implemented'	

#@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name=None):
	return render_template('HW4.html', name=name)

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/users')
def myuserset():
	return str(User.query.all())

@app.route('/users_template')
def users_template():
	return render_template('users_template.html', user=User.query, x=0)

@app.route('/robot/go/<length>')
def picaxe_line(length=None):
	return render_template('picaxe.html', length=length)	

@app.route('/robot/square/<size>')
def picaxe_square(size=None):
	return render_template('picaxe_square.html', size=size)	

	
if __name__ == '__main__':
    app.run(debug=True)