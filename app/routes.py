from flask import request, jsonify
from app import app, db
from app.models import User, Course, AttendanceLog, Student, Department

@app.route('/users', methods=['GET', 'POST'])
def user_list():
    try:
        if request.method == 'GET':
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            users = User.query.paginate(page=page, per_page=per_page, error_out=False)
            
            if not users.items:
                return jsonify({'message': 'No users found'}), 404

            user_list = [{'id': user.id, 'full_name': user.full_name, 'username': user.username, 'email': user.email} for user in users.items]
            
            pagination_info = {
                'total_pages': users.pages,
                'current_page': users.page,
                'per_page': per_page,
                'total_users': users.total,
                'has_next': users.has_next,
                'has_prev': users.has_prev
            }

            response_data = {
                'users': user_list,
                'pagination': pagination_info
            }

            return jsonify(response_data)

        elif request.method == 'POST':
            data = request.json

            # Check if required fields are provided in the JSON request
            required_fields = ['full_name', 'username', 'email']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Missing required fields'}), 400

            # Create a new user
            new_user = User(**data)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()  
        return jsonify({'error': str(e)}), 500 

    return jsonify({'message': 'Aborting'}), 405



@app.route('/courses', methods=['GET', 'POST'])
def courses_list():
    try:
        if request.method == 'GET':
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            courses = Course.query.paginate(page=page, per_page=per_page, error_out=False)

            if not courses.items:
                return jsonify({'message': 'No courses found'}), 404

            course_list = [{'id': course.id, 'course_name': course.course_name, 'department_id': course.department_id} for course in courses.items]

            pagination_info = {
                'total_pages': courses.pages,
                'current_page': courses.page,
                'per_page': per_page,
                'total_courses': courses.total,
                'has_next': courses.has_next,
                'has_prev': courses.has_prev
            }

            response_data = {
                'courses': course_list,
                'pagination': pagination_info
            }

            return jsonify(response_data)

        elif request.method == 'POST':
            data = request.json

            
            required_fields = ['course_name', 'department_id']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Missing required fields'}), 400

      
            new_course = Course(**data)
            db.session.add(new_course)
            db.session.commit()

            return jsonify({'message': 'Course created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Aborting'}), 405



@app.route('/attendance_log', methods=['GET', 'POST'])
def attendance_log_list():
    try:
        if request.method == 'GET':
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            logs = AttendanceLog.query.paginate(page=page, per_page=per_page, error_out=False)

            if not logs.items:
                return jsonify({'message': 'No attendance logs found'}), 404

            log_list = [{'id': log.id, 'student_id': log.student_id, 'course_id': log.course_id, 'present': log.present, 'submitted_by': log.submitted_by, 'updated_at': log.updated_at} for log in logs.items]

            pagination_info = {
                'total_pages': logs.pages,
                'current_page': logs.page,
                'per_page': per_page,
                'total_logs': logs.total,
                'has_next': logs.has_next,
                'has_prev': logs.has_prev
            }

            response_data = {
                'attendance_logs': log_list,
                'pagination': pagination_info
            }

            return jsonify(response_data)

        elif request.method == 'POST':
            data = request.json
            required_fields = ['student_id', 'course_id', 'present', 'submitted_by']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Missing required fields'}), 400
            
            new_log = AttendanceLog(**data)
            db.session.add(new_log)
            db.session.commit()

            return jsonify({'message': 'Attendance log created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Aborting'}), 405

@app.route('/students', methods=['GET', 'POST'])
def student_list():
    try:
        if request.method == 'GET':
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            students = Student.query.paginate(page=page, per_page=per_page, error_out=False)

            if not students.items:
                return jsonify({'message': 'No students found'}), 404

            student_list = [{'id': student.id, 'full_name': student.full_name, 'department_id': student.department_id, 'classes': student.classes} for student in students.items]

            pagination_info = {
                'total_pages': students.pages,
                'current_page': students.page,
                'per_page': per_page,
                'total_students': students.total,
                'has_next': students.has_next,
                'has_prev': students.has_prev
            }

            response_data = {
                'students': student_list,
                'pagination': pagination_info
            }

            return jsonify(response_data)

        elif request.method == 'POST':
            data = request.json

            required_fields = ['full_name', 'department_id', 'classes']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Missing required fields'}), 400


            new_student = Student(**data)
            db.session.add(new_student)
            db.session.commit()

            return jsonify({'message': 'Student created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Aborting'}), 405

@app.route('/departments', methods=['GET', 'POST'])
def departments_list():
    try:
        if request.method == 'GET':
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            departments = Department.query.paginate(page=page, per_page=per_page, error_out=False)

            if not departments.items:
                return jsonify({'message': 'No departments found'}), 404

            department_list = [{'id': department.id, 'department_name': department.department_name} for department in departments.items]

            pagination_info = {
                'total_pages': departments.pages,
                'current_page': departments.page,
                'per_page': per_page,
                'total_departments': departments.total,
                'has_next': departments.has_next,
                'has_prev': departments.has_prev
            }

            response_data = {
                'departments': department_list,
                'pagination': pagination_info
            }

            return jsonify(response_data)

        elif request.method == 'POST':
            data = request.json

            required_fields = ['department_name']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Missing required fields'}), 400

            new_department = Department(**data)
            db.session.add(new_department)
            db.session.commit()

            return jsonify({'message': 'Department created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Aborting'}), 405

