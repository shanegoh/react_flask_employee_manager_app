from models import *    # Declare variables from models

# Database access object
class EmployeeDAO:
    def __init__(self, model):
        self.model = model
    
    def findAllUsers(self):
       return Employee.query.all()
        
    def findEmployeeByUsername(self, given_username):
        return Employee.query\
                .filter_by(username = given_username)\
                .first()

    def registerEmployee(self, username, password, role, department):
        employee = Employee(
            username = username,
            password = password,
            role = role,
            department = department
        )
        db.session.add(employee)
        db.session.commit()


class DepartmentDAO:
    def __init__(self, model):
        self.model = model
    
    def findDepartmentByCodeAndORName(self, code, name):
        return Department.query\
                .filter((Department.code == code) | (Department.name == name))\
                .first()
    
    def findDepartmentByCode(self, code):
        return Department.query\
                .filter(Department.code == code)\
                .first()
    
    def addNewDepartment(self, code, name):
        print(code)
        print(name)
        newDept = Department(
            code = code,
            name = name
        )
        db.session.add(newDept)
        db.session.commit()

    def updateDepartment(self, department):
        db.session.merge(department)
        db.session.commit()


# Declare dao object for services.py to use
employee_dao = EmployeeDAO(Employee)
department_dao = DepartmentDAO(Department)