import requests

from core.exceptions.api import InvalidLogin
from core.config import API_HOST, USER_EMAIL, PASSWORD

class LoginApi:
    
    host = API_HOST
    endpoint = 'login'
    
    def __init__(self)->None:
        
        self.url = self.build_url()
    
    def build_url(self)->str:
        
        return self.host + self.endpoint
    
    def make_post_body(self, email:str, senha:str)->dict:
        
        body = {
          "email": email,
          "senha": senha
        }
        
        return body
    
    def make_request(self, body:dict)->dict:
        
        with requests.post(self.url, json=body) as r:
            return r.json()
        
    def get_token(self, resp:dict)->str:
        
        try:
            return resp['access_token']
        except KeyError:
            raise InvalidLogin(f'Login falhou: {resp["message"]}')
        
    def __call__(self, email:str=USER_EMAIL, senha:str=PASSWORD):
        
        body = self.make_post_body(email, senha)
        resp = self.make_request(body)
        
        return self.get_token(resp)
    

get_token = LoginApi()