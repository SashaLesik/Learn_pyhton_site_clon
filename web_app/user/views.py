from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from web_app.user.forms import LoginForm
from web_app.user.models import User
from flask_login import current_user, login_required, login_user, logout_user
from web_app.user.models import db

blueprint = Blueprint('user', __name__)


@blueprint.route('/register', methods=["GET", "POST"])
def register_page():
    form = LoginForm()
    if form.validate():
        username = form.username.data
        password = form.password.data
        new_user = User(username=username)
        new_user.set_password(password)

        if User.query.filter(User.username == username).count():
            flash('Такой пользователь уже есть')
            return redirect(url_for('register'))
        else:
            db.session.add(new_user)
            db.session.commit()
            flash("Thanks for registering!")
            return redirect(url_for('adverts'))
    title = "Регистрация"
    return render_template("registration.html", page_title=title,
                           form=form)


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    title = "Авторизация"

    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['GET', 'POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('adverts'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@blueprint.route('/admin')
@login_required
def admin_index():
    if current_user.is_admin:
        return 'Привет админ'
    else:
        return 'Ты не админ!'
