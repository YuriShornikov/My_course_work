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
       print(res)


    def

# access_token = 'access_token'
# user_id = 'user_id'
vk = VK(access_token, user_id)
# print(vk.users_info())
print(vk.photos_vk_get())


# Загрузка файла с компа на диск, необходимо переделать с вк на диск
# class Yandex:
#     base_host = 'https://cloud-api.yandex.net/'
#
#     def __init__(self, token: str):
#         self.token = token
#
#     def get_headers(self):
#         return {
#             'content-type': 'application/json',
#             'Authorization': f'OAuth {self.token}'
#         }
#
#     def get_upload_link(self, path):
#         uri ='v1/disk/resources/upload/'
#         url = self.base_host + uri
#         params = {
#             'path': path,
#             'overwrite': True
#         }
#         res = requests.get(url, headers=self.get_headers(), params=params)
#         print(res.json())
#         return res.json()['href']
#
#     def upload(self, local_path, file_path: str):
#         upload_url = self.get_upload_link(file_path)
#         response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
#         if response.status_code == 201:
#             print('Загрузка успешна')
#
# if __name__ == '__main__':
#     path_to_file = os.path.join(os.getcwd(), 't1.jpg')
#     uploader = Yandex(TOKEN)
#     result = uploader.upload(path_to_file, 'test.jpg')