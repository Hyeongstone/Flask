import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# 회원 정보
class Fc_user(db.Model):
    __tablename__ = "fu_user"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))  
    