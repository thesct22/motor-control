# simple hello world flask app

from flask import Flask
from motor_control.rpi import setAngle

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/setBaseAngle/<int:angle>")
def setBaseAngle(angle):
    setAngle.setBaseAngle(angle)
    return "Base angle set to {}".format(angle)


@app.route("/setShoulderAngle/<int:angle>")
def setShoulderAngle(angle):
    setAngle.setShoulderAngle(angle)
    return "Shoulder angle set to {}".format(angle)


@app.route("/setArmAngle/<int:angle>")
def setArmAngle(angle):
    setAngle.setArmAngle(angle)
    return "Arm angle set to {}".format(angle)


# run the app
if __name__ == "__main__":
    app.run()
