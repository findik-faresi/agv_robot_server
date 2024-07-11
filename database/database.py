from flask import Flask
from . import db
from init.init import _init_admin, init_default_qr

def init_db(app: Flask):
    app.config.from_object("config.Config")
    db.init_app(app)

    with app.app_context():
        db.create_all()
        _init_admin(db)
        init_default_qr(db)
