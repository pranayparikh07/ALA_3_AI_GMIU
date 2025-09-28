from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Configure Gemini API with key from .env
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("⚠️ GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

# Choose a supported model
# From docs, examples include: "gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash", etc. :contentReference[oaicite:1]{index=1}
MODEL_NAME = "gemini-2.5-flash"  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/models", methods=["GET"])
def list_models():
    """Optional route: list available models and their supported generation methods."""
    try:
        models = genai.list_models()  # get all models
        # Filter / simplify output
        model_list = []
        for m in models:
            model_list.append({
                "name": m.name,
                "description": getattr(m, "description", ""),
                "supported_methods": getattr(m, "supported_generation_methods", []),
            })
        return jsonify({"models": model_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "⚠️ No message received"}), 400
    try:
        # Use a supported model
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(user_message)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"⚠️ Error: {str(e)}"
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
