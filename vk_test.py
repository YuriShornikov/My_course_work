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


access_token = 'vk1.a.2aPHcgX1vDtWtPNSjinBUOBcbnVMVhWSWGdpVSmVPt149eSSXqU6GTbQ_F6IOV2b_S0rQRhPCCqMSLMa8r0qQ2Mb1P4itHvmEcpIIuqlyoPtwAhfFCdoz7gTgVCAsqoqKk3EhigX-wDA7efHqVrUIodaBjjEccTaYjknQxkNbB24rAxmcP35onAXpsqXtzWziZCOQVk3gMkGkBBGvn_N5Q'
user_id = 51484145
vk = VK(access_token, user_id)
print(vk.users_info())