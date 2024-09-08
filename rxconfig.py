import os
from decouple import config 

DATABASE_URL = config("DATABASE_URL")
RAILWAY_PUBLIC_DOMAIN = os.getenv("RAILWAY_PUBLIC_DOMAIN", "default-domain")

class ReflextemplateConfig(rx.Config):
    pass

config = ReflextemplateConfig(
    app_name="reflex_gpt",
    telemetry_enabled=False,
    frontend_port=3000, 
    backend_port=8000, 
    api_url=f'https://{RAILWAY_PUBLIC_DOMAIN}/backend',
    db_url=DATABASE_URL
)
