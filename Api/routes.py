from flask import Flask, request, jsonify
from Api import app
from flask_restful import Resource
from Api.models import Employees
from Api import db, api
from datetime import datetime
from calendar import monthrange




class Employee(Resource):

    def post(self):
        emp_data = request.get_json()
        emp_exist = Employees.query.filter_by(email=emp_data['email']).first()
        if emp_exist:
            return f'This email is exists!!'
        date_obj = datetime.strptime(emp_data['working_since'], "%m/%d/%Y")
        days = monthrange(date_obj.year, date_obj.month)
        total_days_working = days[1] - date_obj.day
        salary_per_exp = emp_data['salary'] / total_days_working
        new_emp = Employees(name=emp_data['name'], email=emp_data['email'], working_since=emp_data['working_since'], salary=emp_data['salary'], salary_per_exp=salary_per_exp)
        db.session.add(new_emp)
        db.session.commit()

        return new_emp.json()
    
        
        
    def get(self):
        emp = []
        email = request.args.get('email')
        if not email:
            employee_list = Employees.query.all()
        else:
            employee_list = Employees.query.filter_by(email=email)
        for movie in employee_list:
            emp.append({'working_since': movie.working_since, 'salary': movie.salary, 'salary_per_exp': movie.salary_per_exp, 'name': movie.name, 'email':movie.email})

        return jsonify({'employees': emp})
    
        
api.add_resource(Employee, '/')