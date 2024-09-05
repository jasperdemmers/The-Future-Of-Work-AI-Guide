from flask import Flask
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

