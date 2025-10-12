# src/tasks/config.py

from pathlib import Path

class Config:
    def __init__(self):
        self.db_path = Path.home() / ".tasks_db.json"   # or any path you like
        self.db_type = "tiny"  # MUST be either "tiny" or "mongo"

def get_config():
        return Config()
