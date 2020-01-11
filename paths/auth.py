from urllib import request

from flask import Blueprint, session, render_template, redirect
from Database.database import db


from services import auth

app = Blueprint('auth', __name__)

# @app.route('/auth/login')
# def login(data = None):
#     print(session['username'])
#     return render_template('index.html', **locals())


@app.route('/auth/home')
def login(data=None):
    if 'username' in session.keys():
        print('herer code', session['username'])
        user = db.users.find_one({'username': session['username']})
        print('user data, ', user)
        if user['rank']=='1':
            return  redirect('/branch/home')
        elif user['rank'] == '2':
            return redirect('/auth/login')
        elif user['rank'] == '3':
            return  redirect('/head/home')
        elif user['rank'] == '4':
            return  redirect('/admin/home')

    return render_template('login.html', **locals())


@app.route('/auth/validation-login-info', methods=['POST', 'GET'])
def validation_login_info():
    if request.method == 'POST':
        data = request.form
        flag, user = auth.validation(data)
        print(flag, user, ' printing from validation ')
        if flag == False:
            return redirect('/auth/login/')
    session['username'] = user['username']
    return redirect('/auth/home')


@app.route('/auth/logout')
def logout():
    if 'username' in session.keys():
        session.pop('username')
    return redirect('/')