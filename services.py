from daos import *
from auth import generatePWDHash

# Service Layer
# Business logics
class EmployeeService:
    def getAllUsers(self):
        return employee_dao.findAllUsers()
    
    def getEmployeeByUsername(self, given_username):
        return employee_dao.findEmployeeByUsername(given_username)

    def registerEmployee(self, username, password, role, department):
        return employee_dao.registerEmployee(username, generatePWDHash(password), role, department)


class DepartmentService:
    def getDepartmentByCodeAndORName(self, code, name):
        return department_dao.findDepartmentByCodeAndORName(code, name)
    
    def getDepartmentByCode(self, code):
        return department_dao.findDepartmentByCode(code)
    
    def addNewDepartment(self, code, name):
        return department_dao.addNewDepartment(code, name)

    def updateDepartment(self, department, name):
        department.name = name
        return department_dao.updateDepartment(department)