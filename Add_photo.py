import requests

import os

from token_ya import TOKEN

from token_vk import access_token
from token_vk import user_id

# from token import TOKEN


#Получать фото с профиля

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}
   #
   # def users_info(self):
   #     url = 'https://api.vk.com/method/users.get'
   #     params = {'user_ids': self.id}
   #     response = requests.get(url, params={**self.params, **params})
   #     return response.json()

   def photos_vk_get(self, offset=0, count=5):
       url_photos = 'https://api.vk.com/method/photos.get'
       params = {
           'owner_id': 117971802,
           'album_id': 'profile',
           'extended': 1,
           'photo_sizes': 0,
           'offset': offset,
           'count': count,
       }
       res = requests.get(url_photos, params={**self.params, **params}).json()
       return res

       #
       # # print(res)
       # href_photo = {}
       # for keys in res["response"]["items"]:
       #     file_url = keys["sizes"][-1]["url"]
       #     file_name = keys["likes"]["count"]
       #     href_photo[file_name] = file_url
       #
       # return href_photo

# access_token = 'access_token'
# user_id = 'user_id'
vk = VK(access_token, user_id)
# print(vk.users_info())
my_photos = vk.photos_vk_get()
# print(my_photos)
# print(my_photos["response"]["items"])
def get_photo():
    my_photos = vk.photos_vk_get()
    count_photo = my_photos["response"]["count"]
    i = 0
    count = 5
    href_photo = {}
    while i <= count_photo:
        if i != 0:
            my_photos = vk.photos_vk_get(offset=i, count=count)
        for keys in my_photos["response"]["items"]:
			file_url = keys["sizes"][-1]["url"]
			file_name = keys["likes"]["count"]
            href_photo[file_name] = file_url


# vk_href = vk.photos_vk_get()
# vk_href = vk.photos_vk_get(offset=5, count=5)


# print(vk_href)
# print(vk.get_photos())


# Загрузка файла с компа на диск, необходимо переделать с вк на диск
class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, ya_path):
        uri ='v1/disk/resources/upload/'
        url = self.base_host + uri
        params = {
            'path': ya_path,
            'overwrite': True
        }
        res = requests.get(url, headers=self.get_headers(), params=params)
        print(res.json())
        return res.json()['href']

    def upload(self, local_path, file_path: str):
        upload_url = self.get_upload_link(file_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка успешна')

    def upload_from_vk(self, vk_url, ya_url):
        url = 'v1/disk/resources/upload/'
        upload_url = self.base_host + url
        params = {'url': vk_url, 'path': ya_url}
        res = requests.post(upload_url, params=params, headers=self.get_headers())
        print(res.json())

    def create_folder(self, ya_path):
        folder_url = self.base_host + 'v1/disk/resources/'
        params = {'path': ya_path}
        res = requests.put(folder_url, params=params, headers=self.get_headers())


if __name__ == '__main__':
    uploader = Yandex(TOKEN)
    # sop = 10
    # print(vk_href)
    # uploader.create_folder('vk_photo')
    # for key, value in vk_href.items():
    #     uploader.upload_from_vk(vk_href[key], "/vk_photo/%s" % key)
