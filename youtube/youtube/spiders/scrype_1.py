'''
import dryscrape
from bs4 import BeautifulSoup
session = dryscrape.Session()
session.visit(my_url)
response = session.body()
soup = BeautifulSoup(response)
print(soup.find(id="intro-text"))
# Result: <p id="intro-text">Yay! Supports javascript</p>
'''
'''
from requests_html import HTMLSession


url = 'http://www.youtube.com/channel/UCZF6XvqkFb9lURwIPePFU5w/about'
session = HTMLSession()
r = session.get(url)
r.html.render(timeout=30)
print(r.html.text)
'''
from requests_html import HTMLSession  
session = HTMLSession()    
r = session.get('https://www.iwannabechef.ru')  
r.html.render()

print(r.html.text)
titles = r.html.find('.post-title.entry-title')
  
for title in titles:  
    print(title.text, ':', title.absolute_links.pop())

