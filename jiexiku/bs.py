from bs4 import BeautifulSoup

html = ''
with open('ex1.html', 'r',encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')
print(soup.title.name)

print(soup.p.contents)