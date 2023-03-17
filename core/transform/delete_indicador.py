from core.transform import find_id_indicador
from core.api import API

class DeleteIndicadorIfExists:

    tipos = {'iniciativa', 'meta'}

    def __init__(self, api=None):

        self.api = api or API()

    def check_tipo(self, tipo:str)->None:

        if tipo not in self.tipos:
            raise ValueError(f'Tipo must be in {self.tipos}')

    def delete_indicador(self, codigo:str, tipo:str)->bool:

        id_indicador = find_id_indicador(codigo, tipo)

        if id_indicador:
            delete = self.api.delete('indicador', id_indicador)
            if delete:
                return True
        
        return False
    
    def __call__(self, codigo:str, tipo:str)->bool:

        self.check_tipo(tipo)

        return self.delete_indicador(codigo, tipo)

    

    
