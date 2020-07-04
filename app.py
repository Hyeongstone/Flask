import os
from flask import Flask, request, render_template, redirect
from models import db

from models import Fc_user

from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm() # form 생성
    if form.validate_on_submit(): #유효성 검사
        fc_user = Fc_user()
        fc_user.userid = form.data.get('userid')
        fc_user.username = form.data.get('username')
        fc_user.password = form.data.get('password')

        db.session.add(fc_user)
        db.session.commit()
        print('success')

        return redirect("/")

    return render_template('register.html', form=form)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFYCATIONS'] = False 
    app.config['SECRET_KEY'] = 'qwerqerqwerqwer'

    csrf = CSRFProtect()
    csrf.init_app(app)
    #db초기화
    db.init_app(app)
    db.app = app
    #db생성
    db.create_all()

    app.run(host="127.0.0.1", port="5000", debug=True)