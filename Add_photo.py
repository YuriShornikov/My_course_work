import requests

from token_ya import TOKEN

from token_vk import access_token
from token_vk import user_id


import json

#Получать фото с профиля

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}


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

vk = VK(access_token, user_id)

my_photos = vk.photos_vk_get()

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
    #
    def upload_from_vk(self, vk_url, ya_url):
        url = 'v1/disk/resources/upload/'
        upload_url = self.base_host + url
        params = {'url': vk_url, 'path': ya_url}
        res = requests.post(upload_url, params=params, headers=self.get_headers()).json()
        # return res

    def create_folder(self, ya_path):
        folder_url = self.base_host + 'v1/disk/resources/'
        params = {'path': ya_path}
        res = requests.put(folder_url, params=params, headers=self.get_headers())



if __name__ == '__main__':
    uploader = Yandex(TOKEN)

    count_photo = my_photos["response"]["count"]
    print(count_photo)
    i = 0
    count = 5
    photo = []
    while i <= count_photo:
        my_photos = vk.photos_vk_get(offset=i, count=count)
        href_photo = {}
        photo_data ={}
        for keys in my_photos["response"]["items"]:
            file_url = keys["sizes"][-1]["url"]
            uploader.create_folder('vk_photo')
            file_name = keys["likes"]["count"]
            href_photo[file_name] = file_url
            photo_data = {"file_name": f"{file_name}.jpg", "size": keys["sizes"][0]["type"]}
            photo.append(photo_data)

        photo_json = json.dumps(photo, indent=1)
        for key, value in href_photo.items():
            uploader.upload_from_vk(href_photo[key], "/vk_photo/%s" % key)
        print(href_photo)
        i += 5
    print(photo_json)

