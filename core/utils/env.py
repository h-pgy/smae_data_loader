from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

def get_env_var(var_name:str)->str:

    return os.environ[var_name]