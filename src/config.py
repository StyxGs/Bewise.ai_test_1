import os

from dotenv import load_dotenv

load_dotenv()

DB_USER: str = os.environ.get('DB_USER')
DB_PASS: str = os.environ.get('DB_PASS')
DB_HOST: str = os.environ.get('DB_HOST')
DB_PORT: str = os.environ.get('DB_PORT')
DB_NAME: str = os.environ.get('DB_NAME')

DB_USER_TEST: str = os.environ.get('DB_USER_TEST')
DB_PASS_TEST: str = os.environ.get('DB_PASS_TEST')
DB_HOST_TEST: str = os.environ.get('DB_HOST_TEST')
DB_PORT_TEST: str = os.environ.get('DB_PORT_TEST')
DB_NAME_TEST: str = os.environ.get('DB_NAME_TEST')
