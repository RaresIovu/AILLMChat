from flask import Blueprint, request, render_template, jsonify
from knowledge.service import add_knowledge

add_bp = Blueprint("add", __name__)

@add_bp.get("/add")
def add_form():
    return render_template("add_knowledge.html")

@add_bp.post("/add")
def add_form_post():
    subject = request.form.get("subject", "").strip()
    grade = request.form.get("grade", "").strip()
    content = request.form.get("content", "").strip()

    if not (subject and grade and content):
        return "Completați toate câmpurile.", 400

    add_knowledge(subject, grade, content)
    return "Informația a fost adăugată cu succes!"