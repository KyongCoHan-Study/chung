from cgitb import html
from urllib import response
import requests
from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://www.lotteon.com/p/display/main/lotteon'
)

soup = BeautifulSoup(html,'html5lib');
soup.select()