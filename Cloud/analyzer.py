import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Download NLTK data
nltk.download('vader_lexicon')

# Initialize Firebase app with credentials
cred = credentials.Certificate('./routes/valisori-72068-firebase-adminsdk-j493d-a82923bdef.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://valisori-72068-default-rtdb.firebaseio.com'
})

# Get a reference to the database
ref = db.reference()

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

colors_dictionary = {
    1: (255,0,127),
    0.5: (28,232,21),
    0: (255,233,0),
    -0.5: (199,36,177),
    -1: (3,37,126)
}

def associate_color(score):
    rounded_score = min(colors_dictionary.keys(), key=lambda x: abs(x - score))
    color_tuple = colors_dictionary[rounded_score]
    return color_tuple
    
# Function to process the messages
def process_message_and_push(event):
    message = event.data.get('message')
    score = sia.polarity_scores(message)
    color_tuple = associate_color(score)
    ref.child('resulting_color').child('color').set(color_tuple)

# Listen for new messages
ref.child('data').listen(process_message_and_push)