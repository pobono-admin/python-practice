import numpy as np
from pyquery import PyQuery as pq
from lxml import etree




#import urllib
# d = pq("<html></html>")
# d = pq(etree.fromstring("<html></html>"))
d = pq(url='https://tw.yahoo.com/?p=us')
# d = pq(url='http://google.com/', opener=lambda url, **kw: urllib.urlopen(url).read())
# d = pq(filename=path_to_html_file)

print(d('title').text())
crowser_result = d('p').text().encode('utf-8')
print crowser_result

with open('crowser_result.txt', 'w') as crowser:
	crowser.write(crowser_result)


