
import pyrebase
import RPi.GPIO as GPIO

RED_PIN = 15
GREEN_PIN = 18
BLUE_PIN = 27

config = {
    "apiKey": "AIzaSyCiyx86AFTnFwPkjNnI9CIhbG_iov6HuR8",
    "authDomain": "valisori-72068.firebaseapp.com",
    "databaseURL": "https://valisori-72068-default-rtdb.firebaseio.com",
    "storageBucket": "valisori-72068.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

red_pwm = GPIO.PWM(RED_PIN, 100)
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

def set_color(r,g,b):
    red_pwm.ChangeDutyCycle(100)
    green_pwm.ChangeDutyCycle(g*100/255)
    blue_pwm.ChangeDutyCycle(b*100/255)

def stream_handler(message):
    print("intra in functie")
    print(message)
    if message["event"] == "put":
        if message["path"] == "/":
            r,g,b = message["data"]["value"]
            print(r,g,b)
            set_color(r,g,b)

my_stream = db.child("colors").stream(stream_handler)
