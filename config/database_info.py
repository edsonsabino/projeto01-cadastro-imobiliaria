import os
from dotenv import load_dotenv # para buscar .env files

load_dotenv()

database_infos={
    "database": os.getenv("DATABASE"),
    "user": os.getenv("USERNAME"),
    "host": os.getenv("HOST"),
    "password": os.getenv("PASSWORD"),     
}