from flask import Flask, request, jsonify, render_template
from knowledge.routes import knowledge_bp
from chatbot.logic import reply_to_user

app = Flask(__name__, template_folder="templates")
app.register_blueprint(knowledge_bp)

@app.get("/")
def index():
    # Serve HTML that poate conține build-ul React sau pagina simplă; dacă folosești dev React,
    # setează proxy la /api/chat în frontend
    return render_template("chat.html")

@app.post("/api/chat")
def api_chat():
    data = request.get_json(force=True)
    user_msg = data.get('message', '')
    if not user_msg:
        return jsonify({'reply': 'Nu ai trimis niciun mesaj.'}), 400
    reply = reply_to_user(user_msg)
    return jsonify({'reply': reply})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
