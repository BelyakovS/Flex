import pytest
from splinter import Browser
from config_parser import config_db #
import psycopg2
import configparser

#---------URLs
url_ui = "http://10.53.53.160/"
url_charges = 'http://10.53.53.160/charging-api/charges'
url_invoicing = 'http://10.53.53.160/invoicing-api/invoices'

#---------Variables
config = configparser.ConfigParser()
config.read('iflex_config.ini')

login = config.get("settings", "login")
passw = config.get("settings", "password")
auth = config.get("settings", "Authorization")

headers = {
            'Content-Type': 'application/json',
            'Authorization' : auth
          }

#--------Fixtures
# Браузер
@pytest.fixture(scope='class')
def browser():
    browser = Browser('chrome')
    browser.visit(url_ui)
    yield browser

# Подключение к базе
@pytest.fixture(scope="function")
def connect():
  params = config_db()
  connect = psycopg2.connect(**params)
  print("Database opened successfully")
  yield connect
  print("Operation done successfully")
  connect.commit()
  connect.close()
