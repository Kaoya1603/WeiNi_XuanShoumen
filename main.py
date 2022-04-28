from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from data.db_session import global_init, create_session

from models.competition import Competition
from models.orientation import Orientation
from models.user import User
from models.university import University

from forms.login import LoginForm
from forms.register import RegisterForm
from forms.search import SearchForm

app = Flask('__name__')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    global_init('db/competitions.db')

    # from data.competitions import competitions as data
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
    # new_user = User(
    #     surname='Щербина',
    #     name='Софья',
    #     region='Приморский край',
    #     grade=10,
    #     email='sufeiya_vlstar@mail.ru',
    #     password='aoyunhui',
    #     hashed_password='zhongguo'
    # )
    # for i in data:
    #     university = University(
    #         university=i[0],
    #         speciality=i[1],
    #         competition=i[2],
    #         profile=i[3],
    #         subject=i[4],
    #         exam_scores=i[5],
    #         privilege=i[6],
    #         status=i[7],
    #         grade=i[8]
    #     )
    #     db_sess.add(university)
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
            return redirect('/')
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            region=form.region.data,
            grade=form.grade.data,
            email=form.email.data,
            password=form.password.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/search', methods=['GET', 'POST'])
def search():
    db_sess = create_session()
    contest_names = list(x[0] for x in db_sess.query(Competition.competition).distinct().all())
    if request.method == 'GET':
        form = SearchForm()
        return render_template('search.html', title='Поиск ВУЗа', form=form, current_user=current_user,
                               contest_names=contest_names, is_profile_hidden=True, is_table_hidden=True, c=dict())
    if request.method == 'POST':
        form = SearchForm()
        if not form.profile.data:
            a = db_sess.query(Competition.profile).filter(Competition.competition == form.competition.data).all()
            if a:
                form.profile.choices = list(x[0] for x in a)
            else:
                form.profile.errors = ["Олимпиад по вашему запросу не найдено"]
            return render_template('search.html', title='Поиск ВУЗа', form=form, current_user=current_user,
                                   contest_names=contest_names, is_profile_hidden=False, is_table_hidden=True)
        else:
            competition, profile = form.competition.data, form.profile.data
            b = db_sess.query(University).filter(
                University.competition == competition, University.profile == profile).all()
            c = dict()
            for university in b:
                if university.university not in c.keys():
                    c[university.university] = [{university.speciality: [(university.subject, university.exam_scores,
                                                                          university.privilege, university.status,
                                                                          university.grade)]}]
                    c[university.university].append(1)
                elif university.university in c.keys() and university.speciality not in c[university.university][0].keys():
                    c[university.university][0][university.speciality] = [(university.subject, university.exam_scores,
                                                                           university.privilege, university.status,
                                                                           university.grade)]
                    c[university.university][1] += 1
                else:
                    c[university.university][0][university.speciality].append((university.subject, university.exam_scores,
                                                                            university.privilege, university.status,
                                                                            university.grade))
                    c[university.university][1] += 1
            print(c)
            print(len(c['НИУ ВШЭ (Москва)'][0]["Математика"]))
            form.profile.choices = list(x[0] for x in db_sess.query(Competition.profile).filter(
                Competition.competition == form.competition.data).all())
            return render_template('search.html', title='Поиск ВУЗа', form=form, current_user=current_user,
                                   contest_names=contest_names, is_profile_hidden=False, is_table_hidden=False, c=c)


if __name__ == '__main__':
    main()
