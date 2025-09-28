# 🚀 Nova AI – Futuristic Chatbot (Flask + Gemini API)

Nova AI is a modern, **ChatGPT-style chatbot** built using **Flask**, **Google Gemini API**, and a sleek **TailwindCSS frontend**.  
It is designed to give a professional, futuristic SaaS feel – perfect for college assignments, personal projects, or even as a foundation for a real product.

---

## ✨ Features
- 🔑 Secure **API key management** via `.env` file  
- 🖥️ **Flask backend** to handle AI requests  
- 🎨 **TailwindCSS-powered UI** (ChatGPT-like design)  
- ⚡ Press **Enter to send messages** (smooth UX)  
- 🤖 Powered by **Google Gemini** models  
- 📌 Includes **prompt suggestions** for quick start  
- 🧑‍💻 Auto-formatted AI responses (supports paragraphs, lists, code blocks, etc.)

---

## 📂 Project Structure
NovaAI/
│── app.py # Flask backend
│── templates/
│ └── index.html # Chat UI (TailwindCSS + JS)
│── .env # Store your Gemini API key
│── requirements.txt # Python dependencies

---

## 🔧 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/pranayparikh07/ALA_3_AI_GMIU.git
cd ALA_3_AI_GMIU
```
2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Configure Environment Variables
Create a .env file in the project root:
```bash
GEMINI_API_KEY=your_api_key_here
```
5. Run the Flask App
```bash
python app.py
```
🎨 UI & Design

Built with TailwindCSS for a clean, professional SaaS look

Minimal yet futuristic styling (like ChatGPT interface)

Smooth chat bubbles with distinct user and AI message styles
🧪 Example Prompts

Here are some quick prompts you can try in Nova AI:

"Explain Artificial Intelligence in simple words."

"Generate a Python program for a calculator."

"Write a motivational quote about technology."

"Summarize the benefits and risks of AI."

"Help me debug a Flask app error."

📦 Requirements

Python 3.8+

Flask

python-dotenv

google-generativeai

(Already included in requirements.txt)

📜 License

This project is licensed under the MIT License – free to use, modify, and distribute with attribution.

🙌 Acknowledgments

Google Gemini API

Flask

TailwindCSS

🚀 Future Enhancements

✅ Persistent chat history (store in DB)

✅ Multi-user authentication

✅ Export chats as PDF

✅ Deploy on Render / Vercel / Railway
