from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from data.db_session import global_init, create_session

from models.competition import Competition
from models.orientation import Orientation
from models.user import User

from forms.login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    global_init('db/competitions.db')

    # from data.competitions import data
    # db_sess = create_session()
    # for i in data:
    #     new_olymp = Competition(
    #         competition=i[0],
    #         orientation=i[1],
    #         profile=i[2],
    #         subject=i[3],
    #         level=i[4]
    #     )
    #     db_sess.add(new_olymp)
    # db_sess.commit()
    app.run()


@app.route('/')
def index():
    return render_template('index.html', title='Тебе, олимпиадник', current_user=current_user)


@app.route('/competitions')
def competitions():
    db_sess = create_session()

    orientations = db_sess.query(Orientation).all()

    competitions = dict()
    for orientation in orientations:
        competitions[orientation.id] = dict()
        a = db_sess.query(Competition).filter(Competition.orientation == orientation.id).all()
        for olymp in a:
            if olymp.competition not in competitions[orientation.id].keys():
                competitions[orientation.id][olymp.competition] = [(olymp.profile, olymp.subject, olymp.level)]
            else:
                competitions[orientation.id][olymp.competition].append((olymp.profile, olymp.subject, olymp.level))

    return render_template('competitions.html', title='Перечень олимпиад РСОШ', current_user=current_user,
                           orientations=orientations, competitions=competitions)


@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('competitions')
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    main()
