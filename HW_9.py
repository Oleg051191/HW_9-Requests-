import requests
from pprint import pprint
import os

# ЗАДАЧА № 3
url = 'https://api.stackexchange.com/2.3/questions?site=stackoverflow'

def get_all_quuestions(url):
    params = {'sort': 'activity',
              'order': 'desc',
              'fromdate': '1641945600',
              'todate': '1642118400'}

    response = requests.get(url, params=params)
    item_list = response.json()['items']
    path = os.path.join(os.getcwd(), 'Python_q.txt')
    with open(path, 'at', encoding='utf-8') as file:
        count_ques_with_python = 0
        file.write('Все вопросы с тегом "Python"\n')
        for all_dict_in_items in item_list:
            if 'python' in all_dict_in_items['tags']:
                count_ques_with_python += 1
                file.write(all_dict_in_items['title'])
        file.write(f"Всего вопросов на тему 'Python' - {count_ques_with_python}\n")
    print('Список вопросов записан в файл !')


# ЗАДАЧА № 2
class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
                'Content-Type' : 'application/json',
                'Authorization' : 'OAuth {}'.format(self.token)
            }

    def _upload_link(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        headers = self.get_headers()
        response = requests.get(url=url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path, file_name):
        href = self._upload_link(file_path=file_path).get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


TOKEN = ''
Ya = YaUploader(TOKEN)


# ЗАДАЧА № 1
def super_hero():
    url_hulk = 'https://superheroapi.com/api/2619421814940190/332'
    url_Captain = 'https://superheroapi.com/api/2619421814940190/149'
    url_Thanos = 'https://superheroapi.com/api/2619421814940190/655'
    response_h = requests.get(url=url_hulk)
    response_C = requests.get(url=url_Captain)
    response_T = requests.get(url=url_Thanos)
    all_hero = [response_h, response_T, response_C]
    max_int_hero = 0
    for hero in all_hero:
        int_hero = int(hero.json()['powerstats']['intelligence'])
        if max_int_hero <= int_hero:
            max_int_hero = int_hero
            name = hero.json()['name']
    return f"Cамый умный герой - {name}, его интеллект = {max_int_hero}"


if __name__ == '__main__':
    # Задача № 1
    print(super_hero())
    # Задача № 2
    path_to_file = '/Netology/test.txt'
    Ya.upload(path_to_file, 'data.txt')
    # Задача № 3
    get_all_quuestions(url)


