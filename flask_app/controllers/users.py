from flask_app import app

from flask import render_template, request, redirect, session, flash

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

from flask_app.models.user import User


@app.route('/')
def index():

    return redirect("/welcome")




@app.route('/register')
def register_page():

    return render_template("register.html")




@app.route('/user/register', methods=['POST'])
def registered_user():

    if not User.validate(request.form):

        return redirect('/register')

    data = {

        "first_name": request.form ['first_name'],

        "last_name": request.form ['last_name'],

        "email": request.form ['email'],

        "password": bcrypt.generate_password_hash(request.form['password']) 

    }

    id = User.save_user(data)

    session['user_id'] = id

    return redirect ('/dashboard')




@app.route('/login')
def login_page():

    return render_template("login.html")





@app.route('/user/login', methods=['POST'])
def login_user():

    user = User.user_by_email(request.form)


    if not user:

        flash ("Email Not Valid. Please Try Again!" , "login")

        return redirect ('/login')


    if not bcrypt.check_password_hash (user.password, request.form ['password']):

        flash ("Password Not Valid. Please Try Again!", "login")

        return redirect ('/login')


    session ['user_id'] = user.id

    return redirect('/dashboard')





@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')






@app.route('/welcome')
def welcome():

    return render_template("welcome.html")






@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:

        return redirect ('/logout')

    data = {

        'id': session ['user_id']

    }

    return render_template("dashboard.html", user = User.user_by_id(data))




@app.route('/quietus')
def quietus():

    if 'user_id' not in session:

        return redirect ('/logout')

    data = {

        'id': session ['user_id']

    }

    return render_template("quietus.html", user = User.user_by_id(data))





@app.route('/faq')
def faq():

    if 'user_id' not in session:

        return redirect ('/logout')

    data = {

        'id': session ['user_id']

    }

    return render_template("faq.html", user = User.user_by_id(data))




@app.route('/etiquette')
def etiquette():

    if 'user_id' not in session:

        return redirect ('/logout')

    data = {

        'id': session ['user_id']

    }

    return render_template("etiquette.html", user = User.user_by_id(data))





@app.route('/visitus')
def visitus():

    if 'user_id' not in session:

        return redirect ('/logout')

    data = {

        'id': session ['user_id']

    }

    return render_template("visitus.html", user = User.user_by_id(data))