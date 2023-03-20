from core.api import API

class CreateVariable:

    def __init__(self, api=None):

        self.api = api or API()

    def build_payload(self, id_indicador:int, codigo:str):

        payload = {
            "periodicidade": "Mensal",
            "indicador_id": id_indicador,
            "regiao_id" : None,
            "orgao_id": 27,
            "responsaveis" : [6], # Usuario Regina
            "titulo": "Variavel",
            "valor_base": "0",
            "casas_decimais": 2,
            "unidade_medida_id": 1,
            "acumulativa": False,
            "ano_base": 2020,
            "codigo": codigo,
            "inicio_medicao": "2021-01-01",
            "fim_medicao": "2024-12-31",
            "atraso_meses": 1
            }
        
        return payload
    
    def post_create(self, payload:dict)->dict:

        return self.api.post('indicador-variavel', json_body=payload)
    

    def __call__(self, id_indicador:int, codigo_variavel:str)->int:

        payload = self.build_payload(id_indicador, codigo_variavel)

        created = self.post_create(payload)

        id = created.get('id')
        if id is None:
            raise RuntimeError(f'Variavel não criada: {created}')
        return id

    
