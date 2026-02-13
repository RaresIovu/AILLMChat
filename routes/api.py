from flask import Blueprint, request, jsonify
from chatbot.logic import reply_to_user
from knowledge.service import add_knowledge

api_bp = Blueprint("api", __name__)

@api_bp.post("/api/chat")
def api_chat():
    data = request.get_json(force=True)
    user_msg = data.get('message', '')
    user_grd = data.get('grade', '')
    user_sbj = data.get('subject', '')

    if not (user_msg and user_grd and user_sbj):
        return jsonify({'reply': 'Completați toate câmpurile.'}), 400

    reply = reply_to_user(user_msg, user_grd, user_sbj)
    return jsonify({'reply': reply})

@api_bp.post("/api/add_knowledge") 
def api_add_knowledge():
    data = request.get_json(force=True)
    subject = data.get("subject", "").strip()
    grade = data.get("grade", "").strip()
    content = data.get("content", "").strip()

    if not (subject and grade and content):
        return jsonify({"status": "error", "message": "subject, grade și content sunt obligatorii"}), 400

    add_knowledge(subject, grade, content)
    return jsonify({"status": "success"})