from flask import Blueprint, Response

tests_bp = Blueprint("tests", __name__)

@tests_bp.get("/test-diacritice")
def test_diacritice():
    return Response("Șțăîâă – diacritice OK", content_type="text/plain; charset=utf-8")