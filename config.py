from os import getenv

#database config

DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'memory_enhancer'
DB_USER = 'greg'
DB_PASSWORD = getenv('gregDB')

#TG congif
TELEGRAM_TOKEN = getenv('membot')