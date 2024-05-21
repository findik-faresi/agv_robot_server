import json

with open('config.json') as config_file:
    config_data = json.load(config_file)

class Config:
    SQLALCHEMY_DATABASE_URI = config_data['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = config_data['SQLALCHEMY_TRACK_MODIFICATIONS']
