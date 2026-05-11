from flask import Flask
import logging

app = Flask(__name__)

# configuration des logs
logging.basicConfig(filename="app.log", level=logging.ERROR)

@app.route("/")
def home():
    return "✅ Application DevOps + IA fonctionne !"

@app.route("/error")
def error():
    try:
        return 1 / 0  # erreur volontaire
    except Exception as e:
        logging.error(str(e))
        return "❌ Erreur simulée enregistrée", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
