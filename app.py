from flask import Flask, render_template, request
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer 

chatbot = ChatBot('futureBot')
trainer = ChatterBotCorpusTrainer(chatbot) 
trainer.train("chatterbot.corpus.english")

trainer = ListTrainer(chatbot) 
trainer.train([ "How are you?", 'I am good.', 'That is good to hear.', 'Thank you', "You're welcome." ])

response = chatbot.get_response("Hello, how are you?") 
print(response)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html') 

@app.route('/get') 
def get_bot_response(): 
    userText = request.args.get('msg') 
    return str(englishBot.get_response(userText)) 

if __name__ == '__main__': app.run()