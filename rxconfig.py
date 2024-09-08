import reflex as rx
import os
from decouple import config 

DATABASE_URL = config("DATABASE_URL")
railway_public_domain = "RAILWAY_PUBLIC_DOMAIN"

class ReflextemplateConfig(rx.Config):
    pass

config = ReflextemplateConfig(
    app_name="reflex_gpt",
    telemetry_enabled=False,
    frontend_port=3000, # default frontend port
    backend_port=8000, # default backend port
    # Use public domain for API URL if available, otherwise default to local address
    api_url=f'https://{os.getenv(railway_public_domain, "127.0.0.1:8000")}/backend',
    db_url=DATABASE_URL
)
