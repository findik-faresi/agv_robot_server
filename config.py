from helper import read_json

config_data = read_json("config.json")

class Config:
    SQLALCHEMY_DATABASE_URI = config_data['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = config_data['SQLALCHEMY_TRACK_MODIFICATIONS']
