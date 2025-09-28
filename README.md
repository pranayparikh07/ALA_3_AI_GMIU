🚀 Nova AI – Futuristic Chatbot (Flask + Google Gemini API)
Nova AI is a modern, ChatGPT-inspired chatbot powered by Flask, Google Gemini API, and a sleek TailwindCSS frontend. It delivers a professional, futuristic SaaS experience, making it ideal for college assignments, personal projects, or as a foundation for a production-ready product.

✨ Features

🔑 Secure API Key Management: Safely store your Gemini API key in a .env file.
🖥️ Flask Backend: Efficiently handles AI requests and responses.
🎨 TailwindCSS UI: Clean, modern, ChatGPT-like interface with smooth animations.
⚡ Intuitive UX: Press Enter to send messages for a seamless experience.
🤖 Google Gemini Powered: Leverages advanced Gemini models for intelligent responses.
📌 Prompt Suggestions: Preloaded prompts to jumpstart your conversations.
🧑‍💻 Rich Response Formatting: Supports paragraphs, lists, code blocks, and more for clear, readable outputs.


📂 Project Structure
NovaAI/
├── app.py                  # Flask backend for API and routing
├── templates/
│   └── index.html         # TailwindCSS + JavaScript frontend
├── .env                   # Environment variables (Gemini API key)
├── requirements.txt       # Python dependencies


🔧 Setup & Installation
1. Clone the Repository
git clone https://github.com/pranayparikh07/ALA_3_AI_GMIU.git
cd ALA_3_AI_GMIU

2. Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file in the project root and add your Gemini API key:
GEMINI_API_KEY=your_api_key_here


Note: Obtain your Gemini API key from Google Cloud Console or the relevant Gemini API provider.

5. Run the Flask App
python app.py

Access the app at http://localhost:5000 in your browser.

🎨 UI & Design

TailwindCSS-Powered: Minimalistic, futuristic, and responsive design inspired by ChatGPT.
Chat Bubbles: Distinct styles for user and AI messages, with smooth transitions.
Responsive Layout: Works seamlessly on desktop and mobile devices.


🧪 Example Prompts
Try these prompts to explore Nova AI's capabilities:

"Explain Artificial Intelligence in simple terms."
"Write a Python script for a basic calculator."
"Create a motivational quote about technology."
"Summarize the benefits and risks of AI in 100 words."
"Debug a Flask app error with this code: [paste your code]."


📦 Requirements

Python: 3.8 or higher
Dependencies (listed in requirements.txt):
Flask
python-dotenv
google-generativeai



Install all dependencies with:
pip install -r requirements.txt


📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it with proper attribution.

🙌 Acknowledgments

Google Gemini API: For powering the AI capabilities.
Flask: For a lightweight and flexible backend.
TailwindCSS: For the modern, responsive frontend design.


🚀 Future Enhancements

 Persistent Chat History: Store conversations in a database (e.g., SQLite or PostgreSQL).
 Multi-User Authentication: Add user accounts and login functionality.
 Export Chats: Allow users to export conversations as PDF or text files.
 Cloud Deployment: Support for hosting on platforms like Render, Vercel, or Railway.
 Advanced Features: Add voice input/output and real-time collaboration.


📞 Support
For issues, questions, or contributions:

Open an issue on the GitHub repository.
Contact the maintainer: [Your Contact Info, if applicable].

Happy chatting with Nova AI! 🚀
