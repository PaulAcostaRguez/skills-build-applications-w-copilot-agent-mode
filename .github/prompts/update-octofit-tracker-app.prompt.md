---
mode: 'agent'
model: GPT-4.1
---

# Django App Updates

- All Django project files are en el directorio `octofit-tracker/backend/octofit_tracker`.

1. Actualiza `settings.py` para la conexión a MongoDB y CORS.
2. Actualiza `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` y `admin.py` para soportar las colecciones de usuarios, equipos, actividades, leaderboard y workouts.
3. Asegúrate de que `/` apunte a la API y que `api_root` esté presente en `urls.py`.
