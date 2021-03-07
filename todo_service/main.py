from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "hello", 200

if __name__ == '__main__':
    app.run(debug=True)