from flask import render_template, redirect, request, url_for
from app.blueprints.auth.forms.registrationform import RegistrationForm
from app.blueprints.auth.forms.loginform import AuthForm
from flask_login import login_user, current_user, logout_user
from app.repositories.authrepository import AuthRepository
from werkzeug.security import check_password_hash


class AuthController():
    def registration():
        if current_user.is_authenticated:
            return redirect('/')
        
        form = RegistrationForm('/registration/')
        return render_template('auth/registration.html.jinja', form=form)
    
    def create():
        login = request.form.get('login')
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        role_id = 1

        user = AuthRepository.registration(login=login, nickname=nickname, password=password, role_id=role_id)
        remember = True
        login_user(user, remember)
        return redirect(url_for('main.main'))
    
    def login():
        if current_user.is_authenticated:
            return redirect('/')
        
        form = AuthForm()
        return render_template('auth/login.html.jinja', form=form)

    def auth():
        user = AuthRepository.auth(login=request.form["login"])
        remmeber = True if request.form.get('remember') else False

        if user and check_password_hash(user.password_hash, request.form['password']):
            login_user(user, remember=remmeber)
            return redirect('/')
        else:
            return redirect('/login')
        
    def logout():
        logout_user()
        return redirect('/')