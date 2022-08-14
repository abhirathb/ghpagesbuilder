import requests
import os
from enum import Enum 
access_token = os.getenv("access_token")
client_id = os.getenv("client_id")
state = os.getenv('state')
client_secret = os.getenv("client_secret")


class Github:
    _url = "https://api.github.com"
    
    def __init__(self):
        self._url = "https://api.github.com"
    def auth_user(self,token=access_token):
        payload = {
            'client_id': client_id,
            'state': state,
            'allow_signup': 'true'
        }
        #req = requests.get("https://github.com/login/oauth/authorize", params=payload)
        #req.

    def get_access_token(self, code):
        payload = {
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code
        }
        req = requests.post("https://github.com/login/oauth/access_token", params=payload)
        try:
            resp = req.text.split('&')
            for i in resp:
                if 'access' in i:
                    token = i.split('=')[1]
            return token
        except e:
            raise Exception("Failure in acquiring token")

    def get_repos(self, user, token = access_token):
        url = self._url + '/users/' + user + '/repos'
        header = {'Authorization' : 'token ' + access_token}
        req = requests.get(url, headers = header)
        resp = req.json()
        return resp

    def get_tree(self, user, repo, path, token = access_token):
        url = self._url + '/repos/' + user + '/' + repo + '/contents/' + path
        header = {'Authorization' : 'token ' + access_token}
        req = requests.get(url, headers = header)
        resp = req.json()
        return resp

g = Github()
tree = g.get_tree('abhirathb','logfe', '', access_token)
print(tree)
for i in tree:
    print(i['path'])
