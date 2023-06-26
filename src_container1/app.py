from flask import Flask, render_template, request, jsonify
from services import save_text, get_notes


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gDLKWIgkuygwdf23'


@app.route('/', methods=(['POST', 'GET']))
def index():
    if request.method == 'POST':
        save_text(request.form['user_text'])
    return render_template('index.html')


@app.route('/notes', methods=(['POST', 'GET']))
def notes():
    data = {'notes': get_notes()}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
