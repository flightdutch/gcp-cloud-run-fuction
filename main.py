import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Привіт! Це функція на Cloud Run через GitHub CI!"

if __name__ == "__main__":
    # Важливо: порт має братися зі змінної оточення PORT
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
