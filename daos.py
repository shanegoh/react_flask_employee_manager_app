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
    
    def findAllEmployeesFromDepartment(self, code):
        return [row._asdict() for row in Employee.query\
            .join(Department, Employee.department == Department.code)\
            .with_entities(Employee.username, Employee.role, Department.name)\
            .filter(Employee.department == code)\
            .all()]

    #  def reading_list(df:pd.DataFrame)->list:
    #     return list(map(lambda x:Reading(h=x[0],p=x[1]),df.values.tolist()))

    def findEmployeeInfoByUsername(self, username):
        employee = Employee.query\
                .join(Department, Employee.department == Department.code)\
                .with_entities(Employee.id, Employee.username, Employee.role, Department.name, Department.code)\
                .filter((Employee.username == username))\
                .first()
        return EmployeeInfo(employee[0], employee[1], employee[2], employee[3])


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


class SalaryDAO:
    def __init__(self, model):
        self.model = model

    def addEmployeeSalaryAndBonus(self, username, salary, bonus):
        salaryRecord = Salary(
            employee_username = username,
            monthly_salary = salary,
            yearly_bonus = bonus
        )
        db.session.add(salaryRecord)
        db.session.commit()

    def findSalaryInformationByEmployeeUsername(self, username):
        return Salary.query\
                .filter_by(employee_username = username)\
                .first()
    
# Declare dao object for services.py to use
employee_dao = EmployeeDAO(Employee)
department_dao = DepartmentDAO(Department)
salary_dao = SalaryDAO(Salary)