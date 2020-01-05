import requests
from pathlib import Path

BASE_URL = 'http://forum.eve-ru.com/index.php?showtopic=111891&page={page_num}'
BASE_SAVE_PATH = Path('./eve')
#пойтись по страницам и скачать контент
for i in range(1, 4):
    r = requests.get(BASE_URL.format(page_num=i))
    print(r.status_code) # показывает статус ответа
    #print(r.content)     #показывает что внутри
    html_file_path = BASE_SAVE_PATH / 'eve_first_{page_num}.html'.format(page_num=i)
    with open(str(html_file_path.absolute()), 'wb') as f:
        f.write(r.content)
