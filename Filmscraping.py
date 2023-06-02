import requests
from bs4 import BeautifulSoup as be
html="https://www.imdb.com/title/tt0499549/?ref_=nv_sr_srsg_1"
print(html)
film=requests.get(html).content
print(film)
# parser=be(film,"html".parser)
# namaelemenfilm=parser.find("span",attrs={'class':"ipc-chip__text"})
# print(namaelemenfilm.text.replace("\n",""))