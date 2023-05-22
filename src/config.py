import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../test.env')
load_dotenv(dotenv_path=dotenv_path)

dotenv_path_test = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path=dotenv_path_test)

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
