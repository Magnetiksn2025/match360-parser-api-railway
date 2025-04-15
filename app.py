
from flask import Flask, request, jsonify
import os
import tempfile
from PyPDF2 import PdfReader
import spacy

app = Flask(__name__)
nlp = spacy.load("fr_core_news_md")

def extract_text_from_pdf(path):
    text = ""
    try:
        reader = PdfReader(path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        text = ""
    return text.strip()

def parse_with_spacy(text):
    doc = nlp(text)
    email = ""
    tel = ""
    nom = ""
    prenom = ""
    for ent in doc.ents:
        if ent.label_ == "PER":
            nom = ent.text.split()[-1]
            prenom = ent.text.split()[0]
        if ent.label_ == "EMAIL":
            email = ent.text
        if ent.label_ == "PHONE":
            tel = ent.text
    return {
        "prenom": prenom,
        "nom": nom,
        "email": email,
        "telephone": tel,
        "texte_complet": text[:1000]
    }

@app.route("/parse", methods=["POST"])
def parse_cv():
    if "cv" not in request.files:
        return jsonify({"error": "Aucun fichier CV reçu"}), 400

    file = request.files["cv"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        file.save(tmp.name)
        path = tmp.name

    text = extract_text_from_pdf(path)

    parsed = parse_with_spacy(text)
    os.remove(path)
    return jsonify(parsed)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

