from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user

from app import db
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效邮箱或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('已登出')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        flash("用户已注册")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
