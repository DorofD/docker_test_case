from flask import Flask, render_template, request
from services import get_notes


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfgsdaweregrge'


@app.route('/')
def index():
    notes = get_notes()
    return render_template('index.html', notes=notes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
