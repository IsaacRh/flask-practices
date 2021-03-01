from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hi'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hi')
def hello():
    user_ip = request.cookies.get('user_ip')
    return 'Hellor world from flask your ip is {}'.format(user_ip)