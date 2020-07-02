from flask import Flask

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://cuhpqttlfncjia:ab42abc2241221dcd463d198a2c561fe0d1398137ac9945c1c749c5a932a088d@ec2-52-204-232-46.compute-1.amazonaws.com:5432/d2qn5k3635hjih"

import hotels.routes

if __name__ == '__main__':
    app.run(debug=True)
