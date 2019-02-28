# Application configuration file.

import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path('.').resolve()
ENV_PATH = BASE_DIR.joinpath('.env')

load_dotenv(dotenv_path=ENV_PATH)

