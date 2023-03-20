from core.api import API
from core.transform import find_id_iniciativa, find_id_meta

class CreateIndicador:

    #parametros do sistema
    periodicidades = {'Mensal', 'Bimestral', 'Trimestral', 'Quadrimestral', 'Semestral', 'Anual','Quinquenal', 'Secular'}
    polaridade = ['Neutra', 'Positiva', 'Negativa']

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


    def build_payload(self, tipo:str, id:int, codigo:str, titulo:str)->dict:

        payload = {
            "polaridade": "Neutra", #todos neutros por enquanto
            "periodicidade": "Mensal", #todos os dados estão sendo coletados mensalmente
            "codigo": codigo,
            "titulo": titulo,
            "regionalizavel": False, #por enquanto vou criar todos como nao regionalizaveis
            "nivel_regionalizacao": 0,
            "inicio_medicao": "2021-01-01",
            "fim_medicao": "2022-12-31",
            "contexto": "",
            "complemento": "",
            "casas_decimais": 3
        }

        self.add_id_param(payload, tipo, id)

        return payload

    def solve_tipo(self, sheet:dict)->str:

        if sheet['is_iniciativa']:
            return 'iniciativa'
        return 'meta'
    
    def get_id(self, tipo:str, cod:str)->int:

        if tipo == 'meta':
            return find_id_meta(cod)
        return find_id_iniciativa(cod)

    def parse_payload(self, sheet:dict)->dict:
        
        titulo = sheet['titulo']
        codigo = sheet['codigo']
        tipo = self.solve_tipo(sheet)
        id = self.get_id(tipo, codigo)
        payload = self.build_payload(tipo, id, codigo, titulo)

        return payload
    
    def create_indicador(self, sheet:dict)->dict:

        payload = self.parse_payload(sheet)

        return self.api.post('indicador', json_body=payload)
    
    def __call__(self, sheet:dict)->dict:

        return self.create_indicador(sheet)



