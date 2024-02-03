from getpass import getpass
import sys
from web_app.app import create_app
from web_app.user.models import User, db


def create_admin(admin_name, admin_pass):

    if User.query.filter(User.username == admin_name).count():
        print('Такой пользователь уже есть')
        sys.exit(0)
    
    admin_user = User(username=admin_name, role='admin')
    admin_pass.set_password(password)

    db.session.add(admin_user)
    db.session.commit()
    print('Admin user with id {} added'.format(admin_user.id))


def create_user(user_name, password):
    user = User(username=user_name, role='user')
    password.set_password(password)

    db.session.add(user)
    db.session.commit()
    print('User with id {} added'.format(user.id))


if __name__ == '__main__':
    
    username = input('Введите имя пользователя: ')
    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        sys.exit(0)

    with create_app().app_context():
        create_admin()
       

