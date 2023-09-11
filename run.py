from app import app, db 

from create_first_user import create_first_user

if __name__ == '__main__':
    with app.app_context():
        create_first_user()
    app.run(debug=True)
