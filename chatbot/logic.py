from knowledge.service import get_knowledge
from knowledge.embeddings import ensure_index, search_semantic
from .llm_client import generate_answer

# Asigurăm indexul la pornire
ensure_index()



def reply_to_user(question, grade, subject):
    kb_exact = None
    if subject and grade:
        kb_exact = get_knowledge(subject, grade)

    context_parts = []
    if kb_exact:
        context_parts.append(kb_exact)


    sem_results = search_semantic(question, 10, subject, grade)
    for r in sem_results:
        # evităm duplicate identice
        if r['content'] not in context_parts:
            context_parts.append(r['content'])

    if context_parts:
        context = "\n".join(context_parts)
        prompt = f"Context: {context} Question: {question} Answer:"
        # Rares Iovu's logic
        ans = generate_answer(prompt).strip()
        ans = ans.replace(". ", "\n")
        return ans 

    prompt = f"respond exactly with: Nu pot genera un răspuns."
    return generate_answer(prompt)
