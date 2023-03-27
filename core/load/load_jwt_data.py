from .build_jwt_data import BuildJwtData
from core.extract import dados_indicador_gen
from core.api import API


class LoadRealizado:

    def __init__(self):

        self.data_gen = dados_indicador_gen()
        self.build_jwt_payload = BuildJwtData()
        self.api = API()

    def post_data(self, jwtd_payload:dict)->dict:

        self.api.patch('indicador-variavel-serie', json_body=jwtd_payload)

    def itter_data(self):

        for wb in self.data_gen:
            for sheet in wb:
                try:
                    print(sheet['codigo'])
                    jwt_data = self.build_jwt_payload(sheet)
                    posted = self.post_data(jwt_data)
                    print(posted)
                except Exception as e:
                    print(f'Erro: {e}')

    def __call__(self):

        self.itter_data()
