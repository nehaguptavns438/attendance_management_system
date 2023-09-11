from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')  # Load configuration from config.py
db = SQLAlchemy(app)

from app import routes  

if __name__ == '__main__':
    app.run(debug=True)


