import requests

from token_ya import TOKEN

import json

#Подгружаем токен, id приложения, id пользователя
from token_vk import access_token
from token_vk import user_id
from token_ya import vk_id



#Получать фото с профиля

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}


   def photos_vk_get(self,vk_id, offset=0, count=5):
       url_photos = 'https://api.vk.com/method/photos.get'
       params = {
           'owner_id': vk_id,
           'album_id': 'profile',
           'extended': 1,
           'photo_sizes': 0,
           'offset': offset,
           'count': count,
       }
       res = requests.get(url_photos, params={**self.params, **params}).json()
       return res


# Загрузка файла с вк на яндекс диск
class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
#Ссылка для загрузки на яндекс диск
    def upload_from_vk(self, vk_url, ya_url):
        url = 'v1/disk/resources/upload/'
        upload_url = self.base_host + url
        params = {'url': vk_url, 'path': ya_url}
        res = requests.post(upload_url, params=params, headers=self.get_headers()).json()
        # return res

#Создание папки на яндекс диске
    def create_folder(self, ya_path):
        folder_url = self.base_host + 'v1/disk/resources/'
        params = {'path': ya_path}
        res = requests.put(folder_url, params=params, headers=self.get_headers())


#Тело программы с вызовами функций класса
if __name__ == '__main__':
    uploader = Yandex(TOKEN)    #запускаем яндекс класс
    vk = VK(access_token, user_id)    #запускаем вк класс

    my_photos = vk.photos_vk_get(vk_id)    #получаем json фоток вк
    count_photo = my_photos["response"]["count"]
    print(count_photo)    #получаем количество фото
    i = 0
    count = 5
    photo = []    #список для json вывода
    while i <= count_photo:    #запускаем тело цикла для загрузки по 5 фоток, пока i меньше числа фоток, будет работать
        my_photos = vk.photos_vk_get(vk_id, offset=i, count=count)
        href_photo = {}    #словарь для передачи на диск
        photo_data ={}    #словарь для вывода инфы итоговой
        for keys in my_photos["response"]["items"]:
            file_url = keys["sizes"][-1]["url"]    #получаем ссылку с вк для 1 фотки
            uploader.create_folder('vk_photo')    #создаем папку
            file_name = keys["likes"]["count"]    #имя для 1 фото
            href_photo[file_name] = file_url    #добавляем в словарь для яндекса
            photo_data = {"file_name": f"{file_name}.jpg", "size": keys["sizes"][0]["type"]}    #в словарь для ответа
            photo.append(photo_data)    #добавляем в список для ответа


        with open('results.txt', 'w') as outfile:
            photo_json = json.dump(photo, outfile)  # создаем json для ответа
        # for key, value in href_photo.items():
        #     uploader.upload_from_vk(href_photo[key], "/vk_photo/%s" % key)    #передаем фото по ссылке на яндекс диск с именем
        # print(href_photo)    #вывод словарей с 5 фотками для отправки
        i += 5
    print(photo_json)    #вывод ответа

