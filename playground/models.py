from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String(30),index = True, unique = True)
    course_title = db.Column(db.String(30), index = True, unique = True)

class RegisteredStudent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), index = True, unique = True)
    grade = db.Column(db.String(3), index = True, unique = True)
