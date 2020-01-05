import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://forum.eve-ru.com/index.php?showtopic=111891'

r = requests.get(BASE_URL)

soap = BeautifulSoup(r.text, "html.parser")

print(soap.title) #вытаскивает title страницы

msgs = soap.select('div.post.entry-content')

print(len(msgs)) #количество сообщений
print(msgs[-1])  #последнее сообщение

#текст без тегов
parsed_msgs = []

for msg in msgs:
    txt = msg.get_text()
    parsed_msgs.append(txt)

