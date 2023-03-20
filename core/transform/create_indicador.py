from core.api import API

class CreateIndicador:

    tipos = {'meta', 'iniciativa'}

    def __init__(self, api=None)->None:

        self.api = api or API()

    def check_tipo(self, tipo:str)->None:

        if tipo not in self.tipos:
            raise ValueError(f'Tipo must be in {self.tipos}')

    def solve_id_param(self, tipo:str)->str:

        return tipo+'_id'

    def add_id_param(self, payload:dict, tipo:str, id:int)->None:

        id_param_key = self.solve_id_param(tipo)

        id_param = {id_param_key : id}

        payload.update(id_param)

    def build_payload(self, tipo:str, id:int, ):

        payload = {
            "polaridade": "Neutra",
            "periodicidade": "Mensal",
            "codigo": "string",
            "titulo": "string",
            "regionalizavel": False,
            "nivel_regionalizacao": 0,
            "inicio_medicao": "2021-01-01",
            "fim_medicao": "2022-12-31",
            "contexto": "string",
            "complemento": "string",
            "casas_decimais": 30
        }

        self.add_id_param(payload, tipo, id)