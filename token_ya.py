TOKEN = 'y0_AgAAAAAFm3q_AADLWwAAAADUOsbp0lkJ6SxXQZ2CjaM-Ph2t1xcJiwM'
vk_id = 117971802

import requests

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
#     def get_public_resources(self, path):
#         url_public = self.base_host + 'v1/disk/resources/'
#         params = {'overwrite': True, 'path': path}
#         res = requests.get(url_public, params=params, headers=self.get_headers()).json()
#         answer = res['_embedded']['items']
#         return answer
#
#
# if __name__ == '__main__':
#     uploader = Yandex(TOKEN)
#
#     final = uploader.get_public_resources('/vk_photo/')
#     print(final)

# def get_upload_link(self, ya_path):
#     uri ='v1/disk/resources/upload/'
#     url = self.base_host + uri
#     params = {
#         'path': ya_path,
#         'overwrite': True
#     }
#     res = requests.get(url, headers=self.get_headers(), params=params)
#     print(res.json())
#     return res.json()['href']

# def upload(self, local_path, file_path: str):
#     upload_url = self.get_upload_link(file_path)
#     response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
#     if response.status_code == 201:
#         print('Загрузка успешна')

# input('Введите id:')