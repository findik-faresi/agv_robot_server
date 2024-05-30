from flask import Flask
from . import db
from init.init import _init

def init_db(app: Flask):
    app.config.from_object("config.Config")
    db.init_app(app)

    with app.app_context():
        db.create_all()
        _init(db)
