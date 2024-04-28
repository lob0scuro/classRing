from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()



class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    current_value = db.Column(db.Integer, default=0)
    target_value = db.Column(db.Integer, default=int(100000))
    students = db.relationship('Student', backref='admin', lazy=True)
    

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    ring = db.relationship('Ring', backref='student', uselist=False, lazy=True)

    @staticmethod
    def create_with_ring(name, admin_id):
        student = Student(name=name, admin_id=admin_id)
        db.session.add(student)
        db.session.commit()
        # Automatically create a Ring instance for the student
        student.create_ring()
        return student

    def create_ring(self):
        ring = Ring(student_id=self.id, current_value=0, target_value=500)
        db.session.add(ring)
        db.session.commit()

class Ring(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    current_value = db.Column(db.Integer, nullable=False)
    target_value = db.Column(db.Integer, nullable=False)


        