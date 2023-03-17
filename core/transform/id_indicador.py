from core.extract import get_indicadores_api
from core.transform import find_id_iniciativa, find_id_meta

from typing import Callable, Union

class FindIdIndicador:

    tipos = {'meta', 'iniciativa'}

    def check_tipo(self, tipo:str)->None:

        if tipo not in self.tipos:
            raise ValueError(f'Tipo must be in {self.tipos}')

    def solve_id_finder(self, tipo:str)->Callable:

        if tipo == 'meta':
            return find_id_meta
        if tipo == 'iniciativa':
            return find_id_iniciativa
        else:
            raise ValueError(f'Tipo must be in {self.tipos}')

    def find_id(self, codigo:str, tipo:str)->int:

        func = self.solve_id_finder(tipo)

        return func(codigo)

    def find_indicador(self, codigo:str, tipo:str)->dict:

        id = self.find_id(codigo, tipo)
        indicador = get_indicadores_api(id, tipo)

        return indicador
    
    def pipeline(self, codigo:str, tipo:str)->int:

        self.check_tipo(tipo)
        indicador = self.find_indicador(codigo, tipo)

        return indicador.get('id')
    
    def __call__(self, codigo:str, tipo:str)->Union[int, None]:

        return self.pipeline(codigo, tipo)
