import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
   
class Contacts(db.Model):
    __tablename__="contacts"
    contactID = db.Column(db.Integer, primary_key=True)
    fName =db.Column(db.String, nullable=False)
    lName =db.Column(db.String, nullable=False)
    mName =db.Column(db.String, nullable=False)
    workCompany = db.Column(db.String, nullable=True)
    mobile =db.Column(db.String, nullable=False)
    homePhone =db.Column(db.String, nullable=False)
    workPhone =db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    jobTitle = db.Column(db.String, nullable=True) 