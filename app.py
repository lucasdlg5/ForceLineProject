# -*- coding: utf-8 -*-
from flask import Flask, render_template

import os


app = Flask(__name__, template_folder='view')

@app.route("/")
@app.route('/index')
def hello():
     return render_template('index.html')

@app.route('/pagina1/')
def index():
    return render_template('pagina1.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)