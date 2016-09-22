import requests
from bs4 import BeautifulSoup
url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
r_html

soup = BeautifulSoup(r_html, 'html.parser')
print(soup.prettify())