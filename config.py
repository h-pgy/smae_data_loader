from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


#API PARAMETERS
USER_EMAIL = os.environ['USER_EMAIL']
PASSWORD = os.environ['PASSWORD']
API_HOST = 'https://smae-api.appcivico.com/'