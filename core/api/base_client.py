import requests

from core.config import API_HOST, USER_EMAIL, PASSWORD
from core.api import get_token

class BaseAPI:

    def __init__(self, host:str=API_HOST, user_email:str=USER_EMAIL, password:str=PASSWORD):

        self.host = self.__check_host(host)
        self.token = get_token(user_email, password)
        self.headers = self._build_headers(self.token)

    def __check_host(self, host:str)->str:
         
        if not host.endswith('/'):
            host+='/'
        
        return host

    def _build_query_string(self, **params)->str:

        queries = []
        for key, val in params.items():
                query = f'{key}={val}'
                queries.append(query)

        query_string = '&'.join(queries)

        return query_string

    def _build_url(self, endpoint:str, **params)->str:
        
        url = self.host + endpoint

        if params:
            query_str = self._build_query_string(**params)
            url+='?' + query_str
        return url
    
    def _build_headers(self, token:str=None)->dict:
         
        token = token or self.token

        return {'Authorization' : f'Bearer {token}', 'accept' : 'application/json'}

    def get(self, endpoint:str, **query_params)->dict:

        url = self._build_url(endpoint, **query_params)

        with requests.get(url, headers=self.headers) as r:
            return r.json()

    def post(self, endpoint:str, json_body:dict, **query_params)->dict:
        
        url = self._build_url(endpoint, **query_params)

        with requests.post(url, headers=self.headers, json=json_body) as r:
            return r.json()

    def patch(self, endpoint:str, json_body:dict, **query_params)->dict:
        
        url = self._build_url(endpoint, **query_params)

        with requests.patch(url, headers=self.headers, json=json_body) as r:
            return r.json()