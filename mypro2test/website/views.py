from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required, current_user
from .models import Answer,Question,User
from . import db
import json


views=Blueprint('views',__name__)

@views.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('/home',methods=["GET","POST"])
def quesask():
    if request.method=='POST':
        question=request.form.get('question')
        quesdesc=request.form.get('quesdesc')
        tag1=request.form.get('tag1')
        tag2=request.form.get('tag2')
        tag3=request.form.get('tag3')
        new_ques=Question(question=question,quesdesc=quesdesc,tag1=tag1,tag2=tag2,tag3=tag3)
        db.session.add(new_ques)
        db.session.commit()
        return redirect(url_for('views.postques'))
    else:
        allques=Question.query.order_by(Question.date).all()
        return render_template("home.html",post=allques)

@views.route('/home1',methods=["GET","POST"])
@login_required
def postques():
    allques=Question.query.order_by(Question.date).all()
    return render_template("home.html",post=allques)


@views.route('/askquestion')
def aquesk2():
    return render_template('aquestion2.html',user=current_user)




@views.route('/h2',methods=["GET","POST"])
def aans():
    if request.method=='POST':
        answer=request.form.get('answer')
        new_answ=Answer(answer=answer)
        db.session.add(new_answ)
        db.session.commit()
        return redirect(url_for('views.postques'))
    else:
        allansw=Answer.query.order_by(Answer.date).all()
        return render_template("aanswer2.html",postt=allansw)









@views.route('/userprofile')
def userprofile():
    return render_template('user.html', user=current_user)

@views.route('/covid')
def covid():
    return render_template('covid.html', user=current_user)

@views.route('/hijabrow')
def hijabrow():
    return render_template('Hijab Row.html', user=current_user)

@views.route('/f1')
def f1():
    return render_template('F1.html', user=current_user)

@views.route('/vaccination')
def vaccination():
    return render_template('Vaccination.html', user=current_user)


    
@views.route('/onlineclasses')
def onlineclasses():
    return render_template('Online Classes.html', user=current_user)
