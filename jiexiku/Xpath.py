from lxml import etree
import PyMongo

# text = '''
# <div> 
# <ul> 
# <li class="item-0"><a href="linkl.html">first item</a></li> 
# <li class="item-1"><a href="link2.html">second item</a></li> 
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </ul>
# </div>'''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8')) 
html = etree.parse('text.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))
result = html.xpath('//li/a/@href')
print(result)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)