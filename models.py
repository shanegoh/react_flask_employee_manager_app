from dataclasses import dataclass
from db import *

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

#db.create_all()
