
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeePersonal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    dob = db.Column(db.Date)
    address = db.Column(db.String(200))
    work = db.relationship('EmployeeWork', backref='employee', uselist=False)
    bank = db.relationship('EmployeeBankInfo', backref='employee', uselist=False)

class EmployeeWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee_personal.id'))
    department = db.Column(db.String(100))
    designation = db.Column(db.String(100))
    joining_date = db.Column(db.Date)
    performance_score = db.Column(db.Float)
    salary = db.Column(db.Float)

class EmployeeBankInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee_personal.id'))
    bank_name = db.Column(db.String(100))
    account_number = db.Column(db.String(50))
    ifsc_code = db.Column(db.String(20))
    pan_number = db.Column(db.String(20))
    salary_account = db.Column(db.Boolean)
