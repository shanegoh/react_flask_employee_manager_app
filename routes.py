from flask import jsonify, make_response, request
from app import app
from services import *
from utils import *
from auth import *
import sys

# All User
@app.route('/api/login', methods =['POST'])
def login():
    # creates dictionary of form data
    auth = request.form
  
    if not auth or not auth.get(USERNAME) or not auth.get(PASSWORD):
        # returns 401 if any username or / and password is missing
        return make_response({MESSAGE : USERNAME_PASSWORD_EMPTY}, UNAUTHORIZED)
  
    employee = EmployeeService().getEmployeeByUsername(auth.get(USERNAME))
    print(employee)

    if not employee:
        # returns invalid username password
        return make_response({MESSAGE : INVALID_CREDENTIALS_MSG}, UNAUTHORIZED)
    
    if authenticate(employee.password, auth.get(PASSWORD)): 
        return make_response({ACCESS_TOKEN : generateToken(employee, app.config['SECRET_KEY'], algorithm='HS256')}, OK)

    # Default
    return make_response({MESSAGE : INVALID_CREDENTIALS_MSG}, UNAUTHORIZED)


# Manager only (Find all Employees)
@app.route("/api/manager/employees")
@token_required
@manager_required
def findAllEmployees():
    employees = EmployeeService().getAllUsers()
    return make_response(jsonify({ EMPLOYEE_HEADER : employees}), OK)


# Manager Only (Create Department)
@app.route('/api/manager/addDepartment', methods =['PUT'])
@token_required
@manager_required
def addDepartment():
    formData = request.form
  
    if not formData or not formData.get(CODE) or not formData.get(NAME):
        # returns 400 if code or department name is missing
        return make_response({MESSAGE : MISSING_DEPT_NAME_CODE}, BAD_REQUEST)
  
    # verify if department exist
    department = DepartmentService().getDepartmentByCodeAndORName(formData.get(CODE), formData.get(NAME))
    print(department)

    if not department:
        # New record will be created if no update is found
        # means department is new
        DepartmentService().addNewDepartment(formData.get(CODE), formData.get(NAME))
        return make_response({MESSAGE : DEPT_CREATED}, CREATED)
        
    # default returns 400 if department code and/or name exist
    return make_response({MESSAGE : DEPT_EXIST}, BAD_REQUEST)


# Manager Only (Update Department)
@app.route('/api/manager/updateDepartmentName/<code>', methods =['PUT'])
@token_required
@manager_required
def updateDepartment(code):
    formData = request.form
  
    if not formData or not formData.get(NAME):
        # returns 400 if code or department name is missing
        return make_response({MESSAGE : MISSING_DEPT_NAME}, BAD_REQUEST)
  
    # verify if department exist
    department = DepartmentService().getDepartmentByCode(code)
    print(department)

    if department:
        try:
            # means update department
            DepartmentService().updateDepartment(department, formData.get(NAME))
            return make_response({MESSAGE : DEPT_UPDATED}, OK)
        except Exception as e:
            exceptionMsg = str(sys.exc_info()[1]) 
            print(exceptionMsg)
            # update but fail due to over 20 characters string
            return make_response({MESSAGE : LENGTH_LIMIT_ERROR_OR_NAME_EXIST}, BAD_REQUEST)
        
    # default returns 400 if department code and/or name exist
    return make_response({MESSAGE : DEPT_EXIST}, BAD_REQUEST)


# signup route
@app.route('/api/manager/createEmployeeAccount', methods =['POST'])
@token_required
@manager_required
def createEmployeeAccount():
    formData = request.form
    username = formData.get(USERNAME)
    password = formData.get(PASSWORD)
    role = formData.get(ROLE)
    department = formData.get(DEPARTMENT)

    # checking for existing employee
    employee = EmployeeService().getEmployeeByUsername(username)

    if not employee:
        EmployeeService().registerEmployee(username, password, role, department)
        return make_response({MESSAGE : ACCOUNT_CREATED}, CREATED)
    else:
        # returns 202 if user already exists
        return make_response({MESSAGE : ACCOUNT_EXIST}, CONFLICT)