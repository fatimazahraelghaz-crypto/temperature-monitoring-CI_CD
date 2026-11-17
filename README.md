# Système de surveillance de température (CI/CD Demo)

Mini-projet réalisé dans le cadre du module **Testing & CI/CD** (Bachelor GÉSE).

## Fonctionnement
La fonction `check_temperature(tmp)` surveille une température en °C avec un seuil fixé à **30°C** :
- `< 30°C` : renvoie `"NORMAL"`
- `>= 30°C` : renvoie `"ALERT"`