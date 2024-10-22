from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Predefined list of random questions and responses
qa_pairs = [
    {"question": "What is your name?", "response": "I am your AI assistant."},
    {"question": "What is the capital of France?", "response": "The capital of France is Paris."},
    {"question": "Who won the World Cup in 2018?", "response": "France won the World Cup in 2018."},
    {"question": "Tell me a joke.", "response": "Why don't scientists trust atoms? Because they make up everything!"},
    {"question": "What is the meaning of life?", "response": "The meaning of life is to find your purpose and live it."},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message').lower()
    
    # Find the most relevant question (basic matching)
    matched_responses = [qa for qa in qa_pairs if qa['question'].lower() in user_message]
    
    if matched_responses:
        bot_response = random.choice(matched_responses)['response']
    else:
        bot_response = "I don't have an answer for that, but I can learn!"

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
