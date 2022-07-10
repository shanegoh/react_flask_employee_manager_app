from dataclasses import dataclass
from database import db

@dataclass
class Employee(db.Model):
    id: int
    username: str
    password: str
    role: int
    department: int
    deleteFlag: int

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=0)
    department = db.Column(db.Integer, nullable=False, default=0)
    deleteFlag = db.Column(db.Integer, nullable=False, default=0)

@dataclass
class Department(db.Model):
    id: int
    code: int
    name : str

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)   

@dataclass
class Salary(db.Model):
    id: int
    employee_username: str
    monthly_salary: int
    yearly_bonus: int

    id = db.Column(db.Integer, primary_key=True)
    employee_username = db.Column(db.String(20), unique=True, nullable=False) 
    monthly_salary = db.Column(db.Integer, nullable=False, default=0)
    yearly_bonus = db.Column(db.Integer, nullable=False, default=0)

#db.create_all()
