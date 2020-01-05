from  pprint import pprint
import requests

# работа с API HH.ru

BASE_URL = 'https://api.hh.ru/vacancies'

r = requests.get(BASE_URL)
r.json()

#краткая инфа об контенте по ссылке
parsed_json = r.json()['items'][0]
pprint(parsed_json)
print('***'*15)
print('Количество категорий вакансий')
pprint(len(parsed_json))
print('***'*15)
print('Вытаскиваем данные и информацию по интересующей специальности')

#например по Python

interes = requests.get('https://api.hh.ru/vacancies/?text=python')
pprint(interes.json())
print('***'*15)

