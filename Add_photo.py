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
       # print(res)
       # list_photo = []
       href_photo = {}
       for keys in res["response"]["items"]:
           file_url = keys["sizes"][-1]["url"]
           file_name = keys["likes"]["count"]
           # list_photo.append(file_url)
           href_photo[file_name] = file_url
       # print(href_photo)
       # print(list_photo)

           #
           #    print(href_photo)

           # print(file_name)
       # print(href_photo)
       # return file_url, file_name
       return href_photo

       # count_photo = res["response"]["count"]
       # i = 0
       # count = 5
       # photo = []
       # while i <= count_photo:
       #     if i != 0:
       #         data = res(offset=i, count=count)
       #     for files in res["response"]["items"]:
       #         file_url = files["sizes"][-1]["url"]
       #         filename = file_url.split("/")[-1]
       #         photo.append(filename)
       # print(count_photo)


    # def get_photos(self):
    #     data = self.photos_vk_get()
    #     count_photo = data["response"]["count"]
    #     print(count_photo)

# access_token = 'access_token'
# user_id = 'user_id'
vk = VK(access_token, user_id)
# print(vk.users_info())
vk_href = vk.photos_vk_get()

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

if __name__ == '__main__':
    # path_to_file = os.path.join(os.getcwd(), 't1.jpg')
    uploader = Yandex(TOKEN)
    # result = uploader.upload(path_to_file, 'test.jpg')
    for key, value in vk_href.items():
        # print(vk_href[key])
        path = f'/{vk_href[value]}.jpg'
        uploader.upload_from_vk(vk_href[key], path)
