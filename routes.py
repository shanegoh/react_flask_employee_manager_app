from flask import jsonify, make_response
from app import app
from services import *
from utils import *
import json

@app.route("/api/users")
def findAllUsers():
    employees = EmployeeService().getAllUsers()

    return make_response(jsonify({ EMPLOYEE_HEADER : employees}), 200)