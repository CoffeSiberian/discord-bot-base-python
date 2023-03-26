from os import getcwd
from functions.types.settings_types import Settings
import json

working_dir = getcwd()

def getSettingsJson() -> dict:
    with open(f'{working_dir}/settings.json', 'r') as f:
        load = json.load(f)
        f.close()
        return load

def loadSettings() -> Settings:
    return Settings(**getSettingsJson())