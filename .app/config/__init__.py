"""
Declaration of the Settings class and instance that can be used to get any setting required,
using dotenv-settings-handler and python-dotenv.
"""
from typing import Optional

from dotenv import load_dotenv
from dotenv_settings_handler import BaseSettingsHandler

load_dotenv()


class Settings(BaseSettingsHandler):
    host = "127.0.0.1"
    port = 8000
    name = "FastAPI"
    version = "0.0.1"
    log_level = "info"
    description: Optional[str]

    class Config:
        case_insensitive = True
        env_prefix = "API_"


settings = Settings()
