from flask import Flask, render_template
from routes.add import add_bp
from routes.api import api_bp
from routes.tests import tests_bp
import transformers
print(transformers.__version__)

app = Flask(__name__, template_folder="templates")
app.register_blueprint(add_bp)
app.register_blueprint(api_bp)
app.register_blueprint(tests_bp)

@app.get("/")
def index():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
