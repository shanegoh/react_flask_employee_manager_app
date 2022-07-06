# from auth import *
# from flask import jsonify, make_response, request, Blueprint
# from services import *
# from utils import *


# api_manager_bp = Blueprint('api_manager_bp', __name__)

# # Manager only (Find all Employees)
# @api_manager_bp.route("/api/manager/employees")
# @token_required
# @manager_required
# def findAllEmployees():
#     employees = EmployeeService().getAllUsers()
#     return make_response(jsonify({ EMPLOYEE_HEADER : employees}), OK)


# # Manager Only (Create Department)
# @api_manager_bp.route('/api/manager/addDepartment', methods =['PUT'])
# @token_required
# @manager_required
# def addDepartment():
#     formData = request.form
  
#     if not formData or not formData.get(CODE) or not formData.get(NAME):
#         # returns 400 if code or department name is missing
#         return make_response({MESSAGE : MISSING_DEPT_NAME_CODE}, BAD_REQUEST)
  
#     # verify if department exist
#     department = DepartmentService().getDepartmentByCodeAndORName(formData.get(CODE), formData.get(NAME))
#     print(department)

#     if not department:
#         # New record will be created if no update is found
#         # means department is new
#         DepartmentService().addNewDepartment(formData.get(CODE), formData.get(NAME))
#         return make_response({MESSAGE : DEPT_CREATED}, CREATED)
        
#     # default returns 400 if department code and/or name exist
#     return make_response({MESSAGE : DEPT_EXIST}, BAD_REQUEST)


# # Manager Only (Update Department)
# @api_manager_bp.route('/api/manager/updateDepartmentName/<code>', methods=['PUT'])
# @token_required
# @manager_required
# def updateDepartment(code):
#     formData = request.form
  
#     if not formData or not formData.get(NAME):
#         # returns 400 if code or department name is missing
#         return make_response({MESSAGE : MISSING_DEPT_NAME}, BAD_REQUEST)
  
#     # verify if department exist
#     department = DepartmentService().getDepartmentByCode(code)
#     print(department)

#     if department:
#         try:
#             # means update department
#             DepartmentService().updateDepartment(department, formData.get(NAME))
#             return make_response({MESSAGE : DEPT_UPDATED}, OK)
#         except Exception as e:
#             exceptionMsg = str(sys.exc_info()[1]) 
#             print(exceptionMsg)
#             # update but fail due to over 20 characters string
#             return make_response({MESSAGE : LENGTH_LIMIT_ERROR_OR_NAME_EXIST}, BAD_REQUEST)
        
#     # default returns 400 if department code and/or name exist
#     return make_response({MESSAGE : DEPT_EXIST}, BAD_REQUEST)


# # Manager Only (Find employees from particular department)
# @api_manager_bp.route('/api/manager/findAllEmployeesFromDepartment/<code>', methods=['GET'])
# @token_required
# @manager_required
# def findAllEmployeesFromDepartment(code):
#     try:
#         employeeList = EmployeeService().getAllEmployeesFromDepartment(code)
#         print(employeeList)
#         if employeeList:
#             return make_response(jsonify({EMPLOYEE_HEADER : employeeList}), OK)
#         else:
#              return make_response({MESSAGE : EMPLOYEES_NOT_FOUND}, OK)
#     except:
#         exceptionMsg = str(sys.exc_info()[1]) 
#         print(exceptionMsg)
#         return make_response({MESSAGE : GENERIC_ERROR}, BAD_REQUEST)


# # Manager Only (Insert employee salary info)
# @api_manager_bp.route('/api/manager/addEmployeeSalaryAndBonus', methods=['PUT'])
# @token_required
# @manager_required
# def addEmployeeSalaryAndBonus():
#     try:
#         formData = request.form
#         # Check for empty fields
#         if not formData or not formData.get(USERNAME) or not formData.get(SALARY) or not formData.get(BONUS):
#             return make_response({MESSAGE : MISSING_FIELDS}, BAD_REQUEST)
#         else:
#             # Find employee record to ensure they exist
#             employeeRecord = EmployeeService().getEmployeeByUsername(formData.get(USERNAME))
#             if employeeRecord:
#                 salaryRecord = SalaryService().getSalaryInformationByEmployeeUsername(formData.get(USERNAME))
#                 if salaryRecord is None:
#                     SalaryService().addEmployeeSalaryAndBonus(formData.get(USERNAME), formData.get(SALARY), formData.get(BONUS))
#                     return make_response({MESSAGE : SALARY_BONUS_ADD_SUCCESS}, OK)
#                 else:
#                     return make_response({MESSAGE : SALARY_BONUS_EXIST}, BAD_REQUEST)
#             else:
#                 return make_response({MESSAGE : EMPLOYEES_NOT_FOUND}, BAD_REQUEST)
#     except:
#         exceptionMsg = str(sys.exc_info()[1]) 
#         print(exceptionMsg)
#         return make_response({MESSAGE : SALARY_BONUS_ADD_FAIL}, BAD_REQUEST)


# # signup route
# @api_manager_bp.route('/api/manager/createEmployeeAccount', methods =['POST'])
# @token_required
# @manager_required
# def createEmployeeAccount():
#     formData = request.form
#     username = formData.get(USERNAME)
#     password = formData.get(PASSWORD)
#     role = formData.get(ROLE)
#     department = formData.get(DEPARTMENT)

#     # checking for existing employee
#     employee = EmployeeService().getEmployeeByUsername(username)

#     if not employee:
#         EmployeeService().registerEmployee(username, password, role, department)
#         return make_response({MESSAGE : ACCOUNT_CREATED}, CREATED)
#     else:
#         # returns 202 if user already exists
#         return make_response({MESSAGE : ACCOUNT_EXIST}, CONFLICT)