from app import db
class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    submitted_by = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime)


class Course(db.Model):

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(255))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))  
    semester = db.Column(db.String(100))
    classes = db.Column(db.String(100))
    lecture_hours = db.Column(db.Integer)
    submitted_by = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime)


class AttendanceLog(db.Model):

    __tablename__ = 'attendancelog'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))  
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))  
    present = db.Column(db.Boolean)
    submitted_by = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime)


class Student(db.Model):

    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))  
    classes = db.Column(db.String(100))
    submitted_by = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime)


class Department(db.Model):

    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(255))
    submitted_by = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime)
