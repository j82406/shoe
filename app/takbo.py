#print('see')
#from app import appl

#if __name__ == "__main__":
#    app.run()

#from flask import Flask
#from n import a
#appl = Flask(__name__)
from flask import Flask
from flask import render_template
from flask import flash
from flask import redirect
from forms import VectorForm
#from flask_sqlalchemy import SQLAlchemy

appl = Flask(__name__)
appl.config.from_object('config')
#db = SQLAlchemy(appl)

@appl.route('/')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
#def index():
#    return 'HELLO / '
#    user = {'nickname': 'Mig'}  # fake user
#    return render_template('index.html',
#                           title='Home',
#                           user=user)

@appl.route('/loginko', methods=['GET', 'POST'])
def loginko():
#    form = LoginForm()
    return 'wala lang'
#    return render_template('login.html',
#                           title='Sign In',
#                           form=form)

@appl.route('/buhay', methods=['GET', 'POST'])
def login():
    form = VectorForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('inform.html',
                           title='Shoe',
                           form=form,
                           providers=appl.config['OPENID_PROVIDERS'])
#    return 'returnfromlogin'

@appl.route('/hello')
def hello_world():
    return 'Hello, World! i w im yours'
#    return a