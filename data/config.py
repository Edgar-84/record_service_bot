import os
import pathlib
from pathlib import Path
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Data:
    BOT_TOKEN: str
    BASE_DIR: pathlib
    LOGS_BASE_PATH: str


BOT_TOKEN = os.getenv('BOT_TOKEN')
BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_BASE_PATH = os.path.join(BASE_DIR, 'logs/')


data = Data(BOT_TOKEN, BASE_DIR, LOGS_BASE_PATH)
