
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
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def set_color(r,g,b):
    GPIO.output(red_pin, r)
    GPIO.output(green_pin, g)
    GPIO.output(blue_pin, b)

def stream_handler(message):
    print("intra in functie")
    print(message)
    if message["event"] == "put":
        if message["path"] == "/":
            r,g,b = message["data"]["value"]
            print(r,g,b)
            set_color(r/255, g/255, b/255)
            
my_stream = db.child("colors").stream(stream_handler)
