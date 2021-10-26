from flask import Flask, request,flash,url_for
from flask.templating import render_template
from flask_login.utils import _secret_key
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from wtforms.validators import ValidationError
from flask_login import UserMixin, login_manager, login_user, LoginManager, login_required, logout_user, current_user


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "waeccss2021"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///STUDENTSRESPONSESDATABASE.db'


# class StudentsDetails(db.Model):
#     __tablename__= "StudentsSubmissions"
#     id=db.Column(db.Integer(),primary_key=True)
#     FirstName=db.Column(db.String(50), unique=True)
#     SecondName=db.Column(db.String(50), unique=True)
#     IndexNumber =db.Column(db.String(50), unique=True)
#     SchoolNumber =db.Column(db.String(50))
#     Current_School_Name =db.Column(db.String(50))
#     YearGroup =db.Column(db.Integer())
#     FirstChoice =db.Column(db.String(150))
#     SecondChoice =db.Column(db.String(150))
#     ThirdChoice =db.Column(db.String(150))

class Users(db.Model, UserMixin):
    __tablename__ = "login"
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email=db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=True)
    
def __repr__(self):
    return '<Users %r>' % self.email
   
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        login_details = Users(username=username,password = password,email=email)
        #Add to database
        db.session.add(login_details)
        #Save to database
        db.session.commit()
        flash('YOu successfully created an account, login to start the process')
        return redirect(url_for('login'))
    return render_template('sign up.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email=request.form['email']
        password=request.form['password']
        existing_email=Users.query.filter_by(email=email).first()
        if existing_email:
            login_user(existing_email)
            return redirect(url_for('dashboard'))   
        else:
            flash(
            "That email does not exist in our system")
        # return redirect(url_for('dashboard'))
    return render_template('Login.html')



@login_required
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@login_required
@app.route('/selection')
def selection():
    return render_template('selection.html')


# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         FirstName = request.form.get['FirstName']
#         SecondName = request.form.get['SecondName']
#         IndexNumber = request.form.get['IndexNumber']
#         Current_School_Name = request.form.get['Current_School_Name']
#         SchoolNumber= request.form.get['SchoolNumber']
#         YearGroup = request.form.get['YearGroup']
#         FirstChoice = request.form.get['FirstChoice']
#         SecondChoice = request.form.get['SecondChoice']
#         ThirdChoice = request.form.get['ThirdChoice']
#         Studentsdetails=StudentsDetails(FirstName=FirstName, SecondName=SecondName, IndexNumber=IndexNumber,
#         Current_School_Name=Current_School_Name, SchoolNumber=SchoolNumber, YearGroup=YearGroup,
#         FirstChoice=FirstChoice, SecondChoice=SecondChoice, ThirdChoice=ThirdChoice)
#         db.session.add(Studentsdetails)
#         db.session.commit()
#     return render_template('success.html')



if __name__ =='__main__':
    db.create_all()
    app.run(debug=True)