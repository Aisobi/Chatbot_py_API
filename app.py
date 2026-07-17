from flask import Flask, request, jsonify, render_template
from model import predict_class, get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    intents = predict_class(user_message)
    response = get_response(intents)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)model.add(Dropout(0.5))
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])