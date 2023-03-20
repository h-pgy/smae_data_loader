from typing import Callable

from core.api import API
from core.transform import (delete_indicador_if_exists, create_indicador_func, create_variavel_func, 
                        find_id_indicador, find_id_iniciativa, find_id_meta)

class CreateIndicadorAndVariavel:

    tipos = {'iniciativa', 'meta'}

    def __init__(self, api=None)->None:

        self.api = api or API()

    def check_tipo(self, tipo:str)->None:

        if tipo not in self.tipos:
            raise ValueError(f'Tipo must be in {self.tipos}')
        
    def solve_tipo(self, sheet:dict)->str:

        if sheet['is_iniciativa']:
            tipo = 'iniciativa'
        else:
            tipo = 'meta'

        self.check_tipo(tipo)

        return tipo

    def solve_find_id(self, tipo:str)->Callable:

        if tipo == 'meta':
            return find_id_meta
        else:
            return find_id_iniciativa

    def get_id_from_codigo(self, tipo:str, codigo:str)->int:
        
        func = self.solve_find_id(tipo)
        return func(codigo)
    
    def delete_indicador(self, tipo:str, codigo:str)->int:

        deleted = delete_indicador_if_exists(codigo, tipo)
        print(f'Deleted indicador: {deleted}')

    def create_indicaodr(self, sheet:dict)->int:

        created_id = create_indicador_func(sheet)
        if created_id:
            print(f'Created indicador: {created_id}')
        return created_id
    
    def create_variavel(self, codigo:str, id_indicador:int)->int:

        codigo_variavel = 'var_'+codigo
        created_id = create_variavel_func(id_indicador, codigo_variavel)
        if created_id:
            print(f'Created variavel: {created_id}')
        
        return created_id
    
    def pipeline_variavel(self, sheet:dict)->int:

        tipo = self.solve_tipo(sheet)
        codigo = sheet['codigo']

        self.delete_indicador(tipo, codigo)
        id_indicador = self.create_indicaodr(sheet)
        id_variavel = self.create_variavel(codigo, id_indicador)

        return id_variavel
    
    def __call__(self, sheet:dict)->int:

        return self.pipeline_variavel(sheet)
    
