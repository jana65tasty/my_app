from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1>server work</h1><p>time: {datetime.now()}</p>"
