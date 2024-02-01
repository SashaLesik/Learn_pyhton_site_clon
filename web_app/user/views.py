from flask import Blueprint, request, session
from flask import render_template, flash, redirect, url_for
from sqlalchemy import Connection
from web_app.user.forms import LoginForm
from web_app.user.models import User
from flask_login import current_user, login_required, login_user, logout_user
import gc

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/register', methods=["GET", "POST"])
def register_page():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        c, conn = Connection()

        x = c.execute("SELECT * FROM users WHERE username = (%s)", (username))

        if int(x) > 0:
            flash("That username is already taken, please choose another")
            return render_template('register.html', form=form)

        else:
            c.execute("INSERT INTO users (username, password, ) VALUES (%s, %s)",
                      (username, password))
            
            conn.commit()
            flash("Thanks for registering!")
            c.close()
            conn.close()
            gc.collect()

            session['logged_in'] = True
            session['username'] = username

            return redirect(url_for('index.html'))
    title = "Регистрация"
    return render_template("registration.html", page_title=title,
                           form=form)

@blueprint.route('/login')  
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.html'))
    title = "Авторизация"

    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('index.html'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@blueprint.route('/admin')
@login_required
def admin_index():
    if current_user.is_admin:
        return 'Привет админ'
    else:
        return 'Ты не админ!'