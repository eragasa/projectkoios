# dev/spike_fastapi_app_boundary/main.py
from .app import ProjectKoiosApp

app = ProjectKoiosApp.create_app()