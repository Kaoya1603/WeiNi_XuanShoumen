from flask import Flask, render_template
from flask_login import current_user

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', current_user=current_user)


if __name__ == '__main__':
    app.run(port=8080, host='localhost')
