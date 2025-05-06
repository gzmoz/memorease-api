from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Hugging Face modelini buradan yüklüyoruz (Render otomatik indirir)
pipe = pipeline("text2text-generation", model="memorease/memorease-flan-t5")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    inputs = data.get("inputs", "")
    result = pipe(inputs)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
