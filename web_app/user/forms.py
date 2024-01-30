from wtforms.form import UserForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(UserForm):
    username = StringField('Имя пользователя', validators=[DataRequired()],
                           render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()],
                             render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})