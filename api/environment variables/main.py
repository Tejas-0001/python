import os
from dotenv import load_dotenv

load_dotenv(".env")                         # give address to env file you created
t = os.getenv("TG_BOT_TOKEN")               # this environment variable is declared in .env file you used above
print(t)