from flask import Flask, request, jsonify, render_template
from knowledge.routes import knowledge_bp
from chatbot.logic import reply_to_user

app = Flask(__name__, template_folder="templates") # Inițializează serverul web
app.register_blueprint(knowledge_bp) # rutele /add și /api/add_knowledge devin active

@app.get("/")
def index():
    return render_template("chat.html")

@app.post("/api/chat")
def api_chat():
    data = request.get_json(force=True)
    # Rares Iovu's logic
    user_msg = data.get('message', '')
    user_grd = data.get('grade', '')
    user_sbj = data.get('subject', '')
    if not(user_msg or user_grd or user_sbj):
        return jsonify({'reply': 'Completați toate câmpurile.'}), 400
    reply = reply_to_user(user_msg, user_grd, user_sbj)
    return jsonify({'reply': reply})  # 3. Trimite răspunsul profesorului înapoi

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
