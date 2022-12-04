import requests

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


access_token = 'vk1.a.Imtn6XG0-BatbsN-DeI0dpeeaExJhyg580Ha77k55xkwXBFtvqPR0BGoRRzgIMHsiKXlHs3kMnmC0NmuNR4LOPC4f1fRFZHJij3ZRoEMv3pylJyle5cqtIy2GG6ZUpgUNmEQ7Ar5OkiaJyUabkcV'
user_id = 51484145
vk = VK(access_token, user_id)
print(vk.users_info())