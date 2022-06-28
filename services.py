from daos import *

# Service Layer
# Business logics
class EmployeeService:
    def getAllUsers(self):
        return employee_dao.findAllUsers()
         