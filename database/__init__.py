from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
Migrate database:

 - flask db init
 - flask db migrate -m "Initial migration"
 - flask db upgrade 
"""
