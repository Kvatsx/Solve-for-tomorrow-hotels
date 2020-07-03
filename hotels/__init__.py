from flask import Flask

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = ""

import hotels.routes

if __name__ == '__main__':
    app.run(debug=True)
