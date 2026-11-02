## Modification
- API Flask avec les routes /health, /version et /tickets
- 4 tests pytest (health, tickets, route inconnue, version)

## Comment vérifier
1. Créer un venv et installer requirements.txt
2. Lancer `python -m pytest -q` : 4 tests doivent passer
3. Lancer `python app.py` puis tester les routes avec curl
