from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# Hugging Face modelini buradan yüklüyoruz (Render otomatik indirir)
pipe = pipeline("text2text-generation", model="memorease/memorease-flan-t5")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    raw_input = data.get("inputs", "")
    final_prompt = f"Generate a question about: {raw_input}"  # 🧠 Promptu burada yönlendiriyoruz
    result = pipe(final_prompt)
    return jsonify(result)

@app.route("/", methods=["GET"])
def root():
    return "Server is running", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render’ın verdiği portu kullan
    app.run(host="0.0.0.0", port=port)
