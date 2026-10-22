
from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "NLP service is running"})

@app.route("/sentiment", methods=["POST"])
def sentiment():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Please provide some text"}), 400

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        label = "positive"
    elif polarity < 0:
        label = "negative"
    else:
        label = "neutral"

    return jsonify({
        "text": text,
        "sentiment": label,
        "polarity": polarity
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
