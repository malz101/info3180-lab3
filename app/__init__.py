from flask import Flask
from flask_mail import Mail
from .config import Config
import logging
app = Flask(__name__)
app.config.from_object(Config)
# print(repr(app.config))

mail = Mail(app)
from app import views