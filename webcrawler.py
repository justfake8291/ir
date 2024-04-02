#Open cmd Type the following commands 
#  python -m pip install requests 
#  python -m pip install bs4 
#  python -m pip install lxml 




import requests
from bs4 import BeautifulSoup

s = BeautifulSoup(requests.get("https://www.amazon.in").text, features="lxml")

for i in s.find_all("a"):
    print(i.get("href"))