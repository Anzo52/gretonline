from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the home page of Maigret Web Interface.'

if __name__ == '__main__':
    app.run(debug=True)
