from flask import Flask, jsonify, request
from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] =


if __name__ == '__main__':
    app.run(debug=True)