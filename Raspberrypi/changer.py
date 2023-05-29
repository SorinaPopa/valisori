
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

red_pwm = GPIO.PWM(red_pin, 100)
green_pwm = GPIO.PWM(green_pin, 100)
blue_pwm = GPIO.PWM(blue_pin, 100)

def set_color(r,g,b):
    red_pwm.start(red)
    green_pwm.start(green)
    blue_pwm.start(blue)

def stream_handler(message):
    print("intra in functie")
    print(message)
    if message["event"] == "put":
        if message["path"] == "/":
            r,g,b = message["data"]["value"]
            print(r,g,b)
            set_color(r, g, b)
            
            
while True:
    try:
        my_stream = db.child("colors").stream(stream_handler)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
