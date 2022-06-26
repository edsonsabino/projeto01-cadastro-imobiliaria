import os
from dotenv import load_dotenv # para buscar .env files

load_dotenv()

db_infos={
    "database": os.getenv("DATABASE"),
    "user": os.getenv("USUARIO"),
    "host": os.getenv("HOST"),
    "password": os.getenv("PASSWORD")     
}
