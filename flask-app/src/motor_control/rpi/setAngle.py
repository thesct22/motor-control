from time import sleep

import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set up GPIO pins for 4 servo motors

basePin = 3
shoulderPin1 = 5
shoulderPin2 = 7
armPin = 11
testPin = 13

GPIO.setup(basePin, GPIO.OUT)
GPIO.setup(shoulderPin1, GPIO.OUT)
GPIO.setup(shoulderPin2, GPIO.OUT)
GPIO.setup(armPin, GPIO.OUT)
GPIO.setup(testPin, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(testPin, True)

basePWM = GPIO.PWM(basePin, 50)
shoulderPWM1 = GPIO.PWM(shoulderPin1, 50)
shoulderPWM2 = GPIO.PWM(shoulderPin2, 50)
armPWM = GPIO.PWM(armPin, 50)

basePWM.start(0)
shoulderPWM1.start(0)
shoulderPWM2.start(0)
armPWM.start(0)


def setBaseAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(basePin, True)
    basePWM.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(basePin, False)
    basePWM.ChangeDutyCycle(0)


def setShoulderAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(shoulderPin1, True)
    GPIO.output(shoulderPin2, True)
    shoulderPWM1.ChangeDutyCycle(duty)
    shoulderPWM2.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(shoulderPin1, False)
    GPIO.output(shoulderPin2, False)
    shoulderPWM1.ChangeDutyCycle(0)
    shoulderPWM2.ChangeDutyCycle(0)


def setArmAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(armPin, True)
    armPWM.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(armPin, False)
    armPWM.ChangeDutyCycle(0)
