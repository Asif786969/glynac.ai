from flask import jsonify
from flask_restful import Api, Resource
from .models import db, EmployeePersonal, EmployeeWork, EmployeeBankInfo
from faker import Faker
from datetime import date
import random

faker = Faker()

def register_routes(app):
    api = Api(app)
    api.add_resource(GenerateData, '/generate')

class GenerateData(Resource):
    def get(self):
        for _ in range(5):
            # Create employee personal data
            emp = EmployeePersonal(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.unique.email(),
                phone=faker.phone_number(),
                dob=faker.date_of_birth(minimum_age=22, maximum_age=60),
                address=faker.address()
            )
            db.session.add(emp)
            db.session.flush()  # ensures emp.id is available before commit

            # Create work data
            work = EmployeeWork(
                employee_id=emp.id,
                department=random.choice(['Engineering', 'HR', 'Sales', 'Marketing']),
                designation=random.choice(['Manager', 'Executive', 'Intern']),
                joining_date=faker.date_between(start_date='-5y', end_date='-30d'),
                performance_score=round(random.uniform(1.0, 5.0), 2),
                salary=round(random.uniform(30000, 120000), 2)
            )
            db.session.add(work)

            # Create bank info
            bank = EmployeeBankInfo(
                employee_id=emp.id,
                bank_name=random.choice(['HDFC', 'ICICI', 'SBI', 'Axis']),
                account_number=faker.unique.bban(),
                ifsc_code=faker.swift11(),
                pan_number=faker.bothify(text='?????####?'),
                salary_account=random.choice([True, False])
            )
            db.session.add(bank)

        db.session.commit()
        return jsonify({"message": "Generated 5 complete employee records."})
