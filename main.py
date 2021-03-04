from flask import Flask, request, make_response, redirect, render_template, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'secret'

todos = ['TODO 1', 'TODO 2', 'TODO 3']

# CLASS

class LoginForm(FlaskForm):
    user_name = StringField('User name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField('Send', validators=[DataRequired()])

# ERRORS

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


# RUOUTES
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hi'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/hi', methods=['GET', 'POST'])
def hello():
    #user_ip = request.cookies.get('user_ip')
    login_form = LoginForm()
    user_ip = session.get('user_ip')
    user_name = session.get('user_name')
    context = {
        'user_ip' : user_ip,
        'todos': todos,
        'login_form' : login_form,
        'user_name' : user_name,
    }
    if login_form.validate_on_submit():
        user_name = login_form.user_name.data
        session['user_name'] = user_name
        return redirect(url_for('index'))
    # double asteric expand the context
    return render_template('hello.html', **context)