from asyncio import exceptions
from logging import raiseExceptions

import requests



try:
  url = input("enter url")
  response=requests.get(url)
  print(response.status_code)

except requests.exceptions.ConnectionError:
      print("connection error")

except exceptions as e:
    print ("e'")
