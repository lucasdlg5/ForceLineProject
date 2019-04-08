# -*- coding: utf-8 -*-
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "<div id='resposta'>42 é a resposta do universo!!!!!!</div>"
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
