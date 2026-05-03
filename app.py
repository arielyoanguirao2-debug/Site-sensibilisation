from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app) # Indispensable pour autoriser GitHub Pages à envoyer les données

@app.route('/')
def status():
    return "Système de Monitoring en ligne", 200

@app.route('/log_click', methods=['POST'])
def log_click():
    # Récupération de l'IP réelle via le proxy de Render
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    ua = request.headers.get('User-Agent')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Affichage dans la console de Render (Logs)
    print(f"\n[+] NOUVELLE CAPTURE")
    print(f"Date: {date} | IP: {ip}")
    print(f"Appareil: {ua}")
    print("-" * 20)
    
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # Utilisation du port dynamique imposé par l'hébergeur
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
