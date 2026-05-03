from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app) # Indispensable pour que GitHub puisse envoyer les données

@app.route('/')
def home():
    return "Serveur de Monitoring Actif", 200

@app.route('/log_click', methods=['POST'])
def log_click():
    # Récupération de l'IP (Render transmet l'IP réelle via ce header)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    log_entry = f"[{date}] IP: {ip} | UA: {ua}\n"
    
    # Sur un serveur cloud, on écrit dans un fichier persistant 
    # ou on l'affiche simplement dans les logs du tableau de bord
    with open("visites.log", "a") as f:
        f.write(log_entry)
        
    print(f"Nouvelle capture : {ip}")
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run()
