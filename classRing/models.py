from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    ring_id = db.Column(db.Integer, db.ForeignKey('ring.id'), nullable=False)
    ring = db.relationship('Ring', backref=db.backref('students', uselist=False, lazy=True))

    def __repr__(self):
        return f"{self.name}"

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    rings = db.relationship('Ring', backref=db.backref('admin', lazy=True))

    def __repr__(self):
        return f"{self.name}"

class Ring(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    is_master = db.Column(db.Boolean, nullable=False)
    current_value = db.Column(db.Integer, nullable=False)
    target_value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.current_value}/{self.target_value}"