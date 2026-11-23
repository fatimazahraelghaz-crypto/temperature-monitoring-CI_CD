# Système de surveillance de température (CI/CD Demo)

Mini-projet réalisé dans le cadre du module **Testing & CI/CD** (Bachelor GÉSE).

## Fonctionnement
La fonction `check_temperature(tmp)` surveille une température en °C avec un seuil fixé à **30°C** :
- `< 30°C` : renvoie `"NORMAL"`
- `>= 30°C` : renvoie `"ALERT"`
# Surveillance de Température avec CI/CD (GitHub Actions & Pytest)

Ce projet simule un système embarqué de surveillance thermique avec un seuil critique fixé à **30°C** (`< 30°C` : `NORMAL`, `>= 30°C` : `ALERT`).

## Structure du projet
- `temperature.py` : Logique de contrôle de la température.
- `test_temperature.py` : Tests unitaires automatisés (`pytest`) basés sur les valeurs limites (20°C, 29°C, 30°C, 40°C).
- `.github/workflows/tests.yml` : Pipeline CI/CD exécutant les tests à chaque `push` et générant un artifact livrable en cas de succès.