import pyrebase
import RPi.GPIO as GPIO

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

config = {
    "apiKey": "your_api_key",
    "authDomain": "your_project_id.firebaseapp.com",
    "databaseURL": "https://your_project_id.firebaseio.com",
    "storageBucket": "your_project_id.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

red_pwm = GPIO.PWM(RED_PIN, 100)
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)

def set_color(r, g, b):
    red_pwm.start(r * 100 / 255)
    green_pwm.start(g * 100 / 255)
    blue_pwm.start(b * 100 / 255)

def stream_handler(message):
    if message["event"] == "put":
        if message["path"] == "/":
            r, g, b = message["data"]["value"]
            print(r, g, b)
            set_color(r, g, b)

try:
    my_stream = db.child("colors").stream(stream_handler)

    while True:
        pass

except KeyboardInterrupt:
    my_stream.close()
    GPIO.cleanup()
