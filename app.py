from flask import Flask 

app = Flask(__name__)
import config
import routes
import database