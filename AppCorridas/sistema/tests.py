from django.test import TestCase
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from dotenv import load_dotenv
import os

load_dotenv()

session = Session(server_token='TOKEN_UBER')
client = UberRidesClient(session)

response = client.get_products(37.77, -122.41)
products = response.json.get('products')
# Lat = -12.97250699214425
# Long = -38.48438981873865