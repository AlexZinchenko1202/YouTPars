from dotenv import load_dotenv
## using existing module to specify location of the .env file
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# retrieving keys and adding them to the project
# from the .env file through their key names
TOKEN = os.getenv("TOKEN")
user = os.getenv("user")
psw = os.getenv("psw")


TOKEN = '2120757434:AAHes2x0kRE4GFnxU-wEWesIAQ_kXd0ghBg'
user = 'open_windscr'
psw  = '8GKpkWsUMeUbSB6' 