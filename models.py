from dataclasses import dataclass
from db import *

@dataclass
class Employee(db.Model):
    id: int
    username: str
    password: str
    role: int
    deleteFlag: int

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=0)
    deleteFlag = db.Column(db.Integer, nullable=False, default=0)


print("Connecting models")
db.create_all()
