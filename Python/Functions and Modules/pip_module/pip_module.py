import math 
import my_module
print(math.sqrt(5))
print(math.sqrt(16))
print(my_module.greet("Fahim"))

import requests
response = requests.get("https://api.github.com")
print(response.status_code)