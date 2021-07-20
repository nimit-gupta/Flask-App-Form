from flask import Flask, render_template, jsonify, request, redirect
from models import *
from werkzeug.utils import secure_filename
folder_name="static"

app = Flask(__name__, template_folder = 'template')

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@127.0.0.1:3306/test_database_new"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
   contList = Contacts.query.all()
   return render_template("index.html", contList = contList)
    
@app.route("/addcontact", methods=["GET","POST"])
def addcontact():
    fName=request.form.get("FirstName")
    lName=request.form.get("LastName")
    mName=request.form.get("MiddleName")
    workCompany=request.form.get("WorkCompany")
    jobTitle=request.form.get("WorkJobTitle")
    mobile=request.form.get("Mobile")
    homePhone=request.form.get("HomePhone")
    workPhone=request.form.get("WorkPhone")
    email=request.form.get("email")
    contact = Contacts( fName=fName, lName=lName,mName=mName,workCompany=workCompany, jobTitle=jobTitle,mobile=mobile, homePhone=homePhone,workPhone=workPhone,email=email)
    db.session.add(contact)
    db.session.commit()
    return render_template("index.html")

@app.route('/showdetails')
def show_details():
    row = Contacts.query.all()
    return render_template("show.html", row = row)

if __name__ == '__main__':
    app.run(debug = True)
    
