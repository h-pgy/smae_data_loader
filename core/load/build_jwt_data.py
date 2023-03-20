from .pipe_indicador_e_variavel import CreateIndicadorAndVariavel
from core.transform import build_jwt_token
from core.utils.date import mes_to_int


class BuildJwtData:

    def __init__(self, api=None):

        self.criar_variavel = CreateIndicadorAndVariavel(api)

    def get_data(self, sheet:dict)->list:

        return sheet['data']
    
    def build_date(self, data:dict)->str:

        mes = data['mes']
        int_mes = mes_to_int(mes)

        ano = data['ano']

        return f'{ano}-{int_mes}-01'
    
    
    def build_jwt(self, data:dict, id_variavel:int)->str:

        date = self.build_date(data)
        jwt = build_jwt_token('Realizado', id_variavel, date)

        return jwt
    
    def build_payload(self, data:dict, id_variavel:int)->dict:

        valor = data['realizado_mensal']
        jwt = self.build_jwt(data, id_variavel)

        return {'valor' : valor, 'referencia' : jwt}
    
    def build_all_payload(self, all_data:list, id_variavel:int)->list:

        all_payloads = []
        for data in all_data:
            all_payloads.append(self.build_payload(data, id_variavel))

        return all_payloads
    
    def pipeline_payload(self, sheet:dict)->list:

        id_variavel = self.criar_variavel(sheet)
        data = self.get_data(sheet)

        payload = self.build_all_payload(data, id_variavel)

        return payload
    
    def __call__(self, sheet:dict)->list:

        return self.pipeline_payload(sheet)
    

    
    

