#!/bin/bash
echo "[+] Préparation de l'envoi vers GitHub..."
git add .
git commit -m "Mise à jour du serveur permanent"
git push origin main
echo "[+] Terminé ! Render va détecter le changement et redémarrer tout seul."
