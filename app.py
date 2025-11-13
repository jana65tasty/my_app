from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1>server!</h1><p>time: {datetime.now()}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
