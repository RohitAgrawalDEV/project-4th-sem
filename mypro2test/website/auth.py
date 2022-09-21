from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user



auth=Blueprint('auth',__name__)


@auth.route('/login1',methods=["GET","POST"])
def login1():
    if request.method == 'POST':
        usn = request.form.get('usn')
        password = request.form.get('password')

        user = User.query.filter_by(usn=usn).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.postques'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('usn does not exist.', category='error')

    return render_template('login1.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login1'))



@auth.route('/register1',methods=["GET","POST"])
def signup1():
    if request.method =="POST":
        usn=request.form.get('usn')
        email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        user = User.query.filter_by(usn=usn).first()
        if user:
            flash("usn already exist",category='error')
        elif len(usn)<10:
            flash("USN should be of 10 characters",category='error')
        if len(email)<13:
            flash("Enter only bmsce mail",category='error')
        elif password1 != password2:
            flash("Password do not match",category='error')
        elif len(password1)<8:
            flash("Password should be of 8 characters",category='error')
        else:
            new_user=User(usn=usn,email=email,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!",category='success')
            return redirect(url_for('views.home'))


    return render_template('register1.html', user=current_user)



#@auth.route('/login2',methods=["GET","POST"])
#def login2():
#    return render_template('login2.html')


#@auth.route('/logout2')
#def logout2():
    return


#@auth.route('/register2',methods=["GET","POST"])
#def signup2():
    if request.method =="POST":
        tid=request.form.get('tid')
        email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        user = User.query.filter_by(usn=usn).first()
        if user:
            flash("usn already exist",category="error")
        elif len(tid)<10:
            flash("USN should be of 10 characters",category='error')
        if len(email)<13:
            flash("Enter only bmsce mail",category='error')
        elif password1 != password2:
            flash("Password do not match",category='error')
        elif len(password1)<8:
            flash("Password should be of 8 characters",category='error')
        else:
            new_user=User(tid=tid,email=email,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!",category='success')
            return redirect(url_for('views.home'))
    return render_template('register2.html')





#@auth.route('/login3',methods=["GET","POST"])
#def login3():
    return render_template('login3.html')


#@auth.route('/logout3')
#def logout3():
    return


#@auth.route('/register3',methods=["GET","POST"])
#def signup3():
    if request.method =="POST":
        aid=request.form.get('aid')
        email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')


        if len(aid)<10:
            flash("USN should be of 10 characters",category='error')
        if len(email)<13:
            flash("Enter only bmsce mail",category='error')
        elif password1 != password2:
            flash("Password do not match",category='error')
        elif len(password1)<8:
            flash("Password should be of 8 characters",category='error')
        else:
            new_user=User(aid=aid,email=email,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!",category='success')
            return redirect(url_for('views.home'))
    return render_template('register3.html')





#@auth.route('/logreg',methods=["GET","POST"])
#def logreg():
    return render_template('logreg.html')





#@auth.route('/register',methods=["GET","POST"])
#def register():
    return render_template('register.html')
    #