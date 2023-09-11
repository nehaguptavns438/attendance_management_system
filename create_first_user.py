import os
from app import app, db
from app.models import User
import logging

def create_first_user():
    if not User.query.first():
        first_user = User(
            full_name="Admin User",
            username="admin",
            email="admin@example.com",
            password="your_password_here",
            submitted_by="system"  
        )

        db.session.add(first_user)
        db.session.commit()

        logging.info(f"First user password: {first_user.password}")

if __name__ == '__main__':
    with app.app_context():
        create_first_user()
