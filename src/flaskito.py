from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Sequence
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+zxjdbc://dojtest:oracle@10.1.0.201:31521/XE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True  

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, Sequence('post_id_seq'), primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, Sequence('catg_id_seq'), primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class User(db.Model):
    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def index():
    return "New Flaskito rulastonico running on a Java web container."

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='sample'):
    return render_template('hello.html', name=name)
    
@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello2(name='sample2'):
    return render_template('hello2.html', name=name)

db.drop_all()
db.create_all()

admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

py = Category('Python')
p = Post('Hello Python!', 'Python is pretty cool', py)
db.session.add(py)
db.session.add(p)
db.session.commit()

print User.query.filter(User.email.endswith('@example.com')).all()

me = User('me', 'me@example.com')
db.session.add(me)
db.session.commit()

print me.id

db.session.delete(me)
db.session.commit()

if __name__ == "__main__":
    app.run()
