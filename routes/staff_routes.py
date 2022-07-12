from flask import jsonify, make_response, request, Blueprint, current_app as app
from services import *
from utils import *
from auth import *
import sys

staff_routes_bp = Blueprint('staff_routes_bp', __name__)

# Staff only (Find own details)
@staff_routes_bp.route("/findEmployeeInfoById",  methods =['GET']) 
@token_required
@staff_required
def findEmployeeInfoById(username): # username get from decorator
    try:
        employee = EmployeeService().getEmployeeInfoByUsername(username)
        return make_response(jsonify(employee.__dict__), OK)
    except:
        return make_response({MESSAGE : RECORD_NOT_FOUND}, BAD_REQUEST)
   


# Staff only (Find salary details)
@staff_routes_bp.route("/findEmployeePayout",  methods =['GET']) 
@token_required  
@staff_required
def findEmployeePayout(username): # username get from decorator
    try:
        salaryInfo = SalaryService().getSalaryInformationByEmployeeUsername(username)
        return make_response(salaryInfo, OK)
    except:
        app.logger.info("findEmployeePayout: [No Record]")
        return make_response({MESSAGE : RECORD_NOT_FOUND}, BAD_REQUEST)

