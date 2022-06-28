from models import *    # Declare variables from models

# Database access object
class EmployeeDAO:
    def __init__(self, model):
        self.model = model
    
    def findAllUsers(self):
       return Employee.query.all()
        


# Declare dao object for services.py to use
employee_dao = EmployeeDAO(Employee)