
# API de Parsing de CV – Match360 (Railway Edition)

Cette API permet de recevoir un fichier CV (PDF), d’en extraire les données clés avec spaCy, et de retourner un JSON contenant :
- Prénom, Nom
- Email, Téléphone
- Texte brut extrait

## 🚀 Endpoint
POST /parse  
Form-data : `cv` (fichier PDF)

## 🔧 Test local :
pip install -r requirements.txt  
python -m spacy download fr_core_news_md  
python app.py

## 🚀 Déploiement sur Railway
1. Crée un compte sur https://railway.app
2. Crée un nouveau projet > Deploy from GitHub **ou** 'Deploy from Zip'
3. Upload ce projet ou connecte ton dépôt GitHub
4. Paramètres :
   - Build Command : pip install -r requirements.txt && python -m spacy download fr_core_news_md
   - Start Command : python app.py
5. Lance le service et accède à : https://ton-app.up.railway.app/parse
