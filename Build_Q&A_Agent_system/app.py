# app.py
from chatdev import ChatDev, Message
from flask import Flask, request, jsonify, send_from_directory
from transformers import pipeline

app = Flask(__name__)
qa_pipeline = pipeline("question-answering")

# Load extracted Wikipedia content
with open("bangladesh_wiki.txt", "r") as file:
    wiki_content = file.read()

@app.route("/answer", methods=["POST"])
def answer():
    question = request.json.get("question")
    answer = qa_pipeline(question=question, context=wiki_content)
    return jsonify(answer)

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

chatdev = ChatDev()

@chatdev.on_message
def handle_message(message: Message):
    question = message.content
    answer = qa_pipeline(question=question, context=wiki_content)
    message.respond(answer)

if __name__ == "__main__":
    chatdev.run()
    app.run(debug=True)
