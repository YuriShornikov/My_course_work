import requests

from token_vk import access_token
from token_vk import user_id

# from token import TOKEN


#Получать фото с профиля

class VK:

#    def __init__(self, access_token, user_id, version='5.131'):
#        self.token = access_token
#        self.id = user_id
#        self.version = version
#        self.params = {'access_token': self.token, 'v': self.version}
#
#    def users_info(self):
#        url = 'https://api.vk.com/method/users.get'
#        params = {'user_ids': self.id}
#        response = requests.get(url, params={**self.params, **params})
#        return response.json()
#
#
# # access_token = 'access_token'
# # user_id = 'user_id'
# vk = VK(access_token, user_id)
# print(vk.users_info())


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

    def get_upload_link(self, path):
        uri ='v1/disk/resources/upload/'
        url = uri + self.base_host
        params = {
            'path': path,
            'overwrite': True
        }
        res = requests.get(url, headers=self.get_headers(), params=params)
        print(res.json())
        return res.json()['href']

    def get_upload_disk(self, local_path, file_path):
        url_disk = self.get_upload_link(file_path)
        res_disk = requests.put(url_disk, data=open(local_path, 'rb'), headers=self.get_headers())
        print(res_disk.json())
        if res_disk.json() ==201:
            print('Your upload complete')


if __name__ == '__main__':
    TOKEN = 'y0_AgAAAAAFm3q_AADLWwAAAADUOsbp0lkJ6SxXQZ2CjaM-Ph2t1xcJiwM'
    test = Yandex(TOKEN)
    result = test.get_upload_disk('/t1.jpg', '/test.jpg')