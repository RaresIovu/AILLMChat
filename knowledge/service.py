# knowledge/service.py
from database.db import get_connection
from .embeddings import compute_embedding, save_embedding, build_faiss_index, ensure_index

def add_knowledge(subject, grade, content):
    con = get_connection()
    cur = con.cursor()
    # Materia si clasa vor fi introduse in database cu minuscule pentru ca inputul userului sa fie case insensitive
    cur.execute(
        "INSERT INTO knowledge (subject, grade, content) VALUES (LOWER(?), LOWER(?), (?))",
        (subject, grade, content)
    )
    knowledge_id = cur.lastrowid
    con.commit()
    con.close()

    emb = compute_embedding(content)
    save_embedding(knowledge_id, emb)
    # Pentru set mic: rebuild index. Pentru dataset mare: append logic.
    build_faiss_index()
    ensure_index()

#Rares Iovu's logic
def get_knowledge(subject, grade):
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        "SELECT content FROM knowledge WHERE subject = ? AND grade = ?",
        (subject.lower(), grade.lower())
        # Vezi linia 10 
    )
    result = cur.fetchall()
    # Folosim fetchall in loc de fetchone pentru a returna toate contextele de la clasa si materia aleasa
    con.close()
    context = [res[0] for res in result]
    context = "\n".join(line for line in context)
    return context if context else None

# def get_knowledge(subject, grade):
#     con = get_connection()
#     cur = con.cursor()
#     cur.execute(
#         "SELECT content FROM knowledge WHERE subject=? AND grade=?",
#         (subject, grade)
#     )
#     result = cur.fetchone()
#     con.close()
#     return result[0] if result else None
