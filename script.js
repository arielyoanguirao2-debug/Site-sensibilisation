function revealTrap() {
    // On cache la vérification d'âge et on montre la "douche froide"
    document.getElementById('age-gate').style.display = 'none';
    document.getElementById('reveal-screen').style.display = 'flex';

    // REMPLACE par ton lien HTTPS généré par Ngrok (ex: https://a1b2-c3d4.ngrok-free.app)
    const backendURL = "https://TON-LIEN-NGROK.ngrok-free.app/log_click";

    fetch(backendURL, { 
        method: 'POST',
        mode: 'cors'
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('u-ip').innerText = data.ip;
        document.getElementById('u-city').innerText = data.city + " (" + data.isp + ")";
    })
    .catch(err => {
        document.getElementById('u-ip').innerText = "Serveur hors-ligne";
    });
}
