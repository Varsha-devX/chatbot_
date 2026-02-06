'''from ai import get_ai_response
print("welcome to the  AI Chatbot")
print("type exit, quit, or bye to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break
    response = get_ai_response(user_input)
    print("Assistant:", response)'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'
    

if __name__ == '__main__':
    app.run(debug=True)