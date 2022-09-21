from email.policy import default
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(150), unique=True)
  #  aid = db.Column(db.String(150),default='N/A')
 #   tid = db.Column(db.String(150),default='N/A')
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    question = db.relationship('Question')
    answer = db.relationship('Answer')
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(10000),nullable=False)
    quesdesc=db.Column(db.String(100000000),nullable=True)
    tag1=db.Column(db.String(100),nullable=True)
    tag2=db.Column(db.String(100),nullable=True)
    tag3=db.Column(db.String(100),nullable=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_ques_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer = db.relationship('Answer')


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(10000000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    user_ans_id = db.Column(db.Integer, db.ForeignKey('user.id'))