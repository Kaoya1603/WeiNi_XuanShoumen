from flask import Flask, render_template
from flask_login import current_user
from data.db_session import global_init, create_session

from models.competition import Competition
from models.orientation import Orientation

app = Flask(__name__)


def main():
    global_init('db/competitions.db')
    app.run()


@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)


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

    return render_template('competitions.html', current_user=current_user, orientations=orientations,
                           competitions=competitions)


if __name__ == '__main__':
    main()
