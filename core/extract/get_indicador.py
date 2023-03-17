from core.api import API

class GetIndicador:

    tipo_busca = {'meta', 'iniciativa'}

    def __init__(self):

        self.api = API()

    def check_param(self, tipo:str)->None:

        if tipo not in self.tipo_busca:
            raise ValueError(f'Tipo must be in {self.tipo_busca}')

    def solve_param(self, tipo:str)->str:

        self.check_param(tipo)

        return tipo + '_id'

    def build_params(self, id:int, tipo_busca:str)->dict:

        return {self.solve_param(tipo_busca) : id}
    
    def __call__(self, id:int, tipo_busca:str)->dict:

        params = self.build_params(id, tipo_busca)

        indi_list =  self.api.get('indicador', **params).get('linhas')
        
        if indi_list:
            return indi_list[0]
        return {}
