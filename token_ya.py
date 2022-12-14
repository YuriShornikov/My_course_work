TOKEN = 'y0_AgAAAAAFm3q_AADLWwAAAADUOsbp0lkJ6SxXQZ2CjaM-Ph2t1xcJiwM'

import requests

class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_public_resources(self, path_photo):
        url_public = self.base_host + 'v1/disk/resources/download'
        params = {'path': path_photo}
        res = requests.get(url_public, params=params, headers=self.get_headers()).json()
        return res


if __name__ == '__main__':
    uploader = Yandex(TOKEN)

    final = uploader.get_public_resources('/vk_photo')
    print(final)