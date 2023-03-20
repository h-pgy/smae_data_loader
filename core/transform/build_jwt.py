import jwt
from time import time
from core.config import SESSION_JWT_SECRET

class DadosJwt:

    ALGORITHIM = 'HS256'

    tipos_dado = {'Realizado', 'RealizadoAcumulado', 'Previsto', 'PrevistoAcumulado'}

    def __init__(self, expire_seconds = 900, secret=SESSION_JWT_SECRET)->None:

        self.exp = expire_seconds
        self.secret = secret

    def curr_time_epoch(self):

        return int(time())

    def build_payload(self, tipo_realizado:str, id_variavel:int, date:str):

        #value is a string encoded float with '.' as decimal separator
        #date must be in YYYY-MM-DD str format
        payload = {
            "p": date,
            "v": id_variavel,
            "s": tipo_realizado,
            "iat": self.curr_time_epoch(),
            "exp": self.curr_time_epoch() + self.exp
            }
        
        return payload
    
    def gen_jwt(self, payload:str)->str:

        return jwt.encode(payload, self.secret, self.ALGORITHIM)
    
    def __call__(self, tipo_realizado:str, id_variavel:int, date:str)->str:

        payload = self.build_payload(tipo_realizado, id_variavel, date)
        jwt_criado = self.gen_jwt(payload)

        return jwt_criado

    


