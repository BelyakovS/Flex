import pytest
from splinter import Browser
from config_parser import config_db #
import psycopg2

url_ui = "http://10.53.53.160/"
url_api = 'http://10.53.53.160/services-api/tariffs'
login = 'testov'
passw = '1q2w3e'

headers = {
            'Content-Type': 'application/json',
            'Authorization' : 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOjcsInVzZXJfbmFtZSI6InRlc3RvdiIsImxhc3RfbmFtZSI6ItCi0LXRgdGC0L7QsiIsIm1pZGRsZV9uYW1lIjpudWxsLCJkaXNwbGF5X25hbWUiOiLQotC10YHRgtC-0LIg0KLQtdGB0YIiLCJjbGllbnRfaWQiOiJjbGllbnQiLCJ1c2VyX3R5cGUiOiJleHRlcm5hbCIsInVzZXJfaWQiOjEwMDAwMDEsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2MTM0OTAwNzEsImZpcnN0X25hbWUiOiLQotC10YHRgiIsImVtYWlsIjoidGVzdG92QGlmbGV4LnJ1IiwianRpIjoiZTc0NTJjYTUtODZlYi00MDUwLWI0MGQtZDE5YzZkNWVkNDhkIn0.Yfo3pVY_kr8BOrN4Ava1y0yOelBQ8GhcvIX8GhPowrL6YfVu3ChYO38eKycx4G2QhuFaAfP_jpVa0Y2xbFPQ-ovYqz4A_w2QvaDgq2U6fhrcF1PReD2k8Cje7p7GLrmL7TYr0qZ7R7lkLYLnQwhT_UeVjEfCdK4u2CP1Ws7kHj5r19XceXDnAhSdrvzWC7OH9EGLGSgKYWMrGiCts2LsUWdnl6DnTl2BCRgF7T05W5k0opUFPVrh0apDNNWRcHVRbftlJTeB9rKoOPlesyG44ynN5OJPg-AwoOcwG4XdHlOcLr90YQxdO5BI_l37nTSslsiu_rWVR_iDbSy854RUbQ'
          }

@pytest.fixture(scope='class')
def browser():

    browser = Browser('chrome')
    browser.visit(url_ui)
    yield browser

@pytest.fixture(scope="function")
def connect():
  params = config_db()
  connect = psycopg2.connect(**params)
  print("Database opened successfully")
  yield connect
  print("Operation done successfully")
  connect.close()
