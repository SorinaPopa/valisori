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

def set_color(r,g,b):
    GPIO.output(RED_PIN, r)
    GPIO.output(GREEN_PIN, g)
    GPIO.output(BLUE_PIN, b)

def stream_handler(message):
    print("intra in functie")
    print(message)
    if message["event"] == "put":
        if message["path"] == "/":
            print(message["data"])
            r,g,b = message["data"]["value"]
            print(r,g,b)
            set_color(r,g,b)

my_stream = db.child("colors").stream(stream_handler)

print("face ceva")
