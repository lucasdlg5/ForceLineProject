from flask import Flask

import os


app = Flask(__name__)

@app.route("/")
def hello():
    return "42 é a resposta do universo!"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)