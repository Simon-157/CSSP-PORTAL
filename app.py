from flask import Flask, request
from flask.templating import render_template


app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index', methods=['POST'])
def index():
    # if request.method=='POST':
    # username = request.form.get['username']
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    return render_template('success.html')


if __name__ =='__main__':
    app.run(debug=True)