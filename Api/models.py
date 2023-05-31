from enum import unique
from Api import db
import datetime

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    working_since = db.Column(db.Date(), nullable=False, default=datetime.date.today())
    salary = db.Column(db.Integer, nullable=False)
    salary_per_exp = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def json(self):
        return {'id': self.id, 'working_since': str(self.working_since),
                'salary': self.salary, 'salary_per_exp': self.salary_per_exp, 'name':self.name, 'email':self.email}