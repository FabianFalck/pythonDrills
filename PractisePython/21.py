import requests
from bs4 import BeautifulSoup
requests
url = 'http://www.tagesschau.de'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')
soup_prettified = soup.prettify()

with open('text_test_1.html','w') as open_file:
    open_file.write(soup_prettified.encode('ascii', 'replace')) #when you open the html-file, it looks very weird. Why?