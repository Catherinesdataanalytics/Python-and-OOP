import requests

request= requests.get('http://www.johnlewis.com/john-lewis-wade-office-chair-black/p447855')

#print(request.content)

from bs4 import BeautifulSoup

content=request.content

soup= BeautifulSoup(content,'html.parser')

element = soup.find_all("p",{"class":"price"})
print(type(element))
#print(element.text)  #strip())
print(soup.get_text)
for i in element:
    print(i)
#<p class="price price--large">991.00
#print(element.text)