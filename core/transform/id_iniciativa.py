from typing import Union

from core.extract import get_iniciativas_api
from core.transform import find_id_meta

class FindIdIniciativa:

    def clean_codigo(self, codigo:str)->str:
    
        if codigo.startswith('0'):
            codigo = codigo.lstrip('0')
        
        return codigo.rstrip().lower()

    def extract_cod_meta(self, cod_iniciativa:str)->str:

        codigo_limpo = self.clean_codigo(cod_iniciativa)

        cod_meta = codigo_limpo.split('.')[0]

        return cod_meta
    
    def get_id_meta(self, cod_iniciativa:str)->int:

        cod_meta = self.extract_cod_meta(cod_iniciativa)

        return find_id_meta(cod_meta)

    def get_iniciativas_meta(self, cod_iniciativa:str)->list:

        id_meta = self.get_id_meta(cod_iniciativa)

        iniciativas = get_iniciativas_api(id_meta)

        return iniciativas
    
    def gen_iniciativas_mapper(self, iniciativas:list)->dict:

        mapper = {}
        for ini in iniciativas:
            codigo_limpo = self.clean_codigo(ini['codigo'])
            mapper[codigo_limpo] = ini['id']

        return mapper
    
    def pipeline(self, cod_iniciativa:str)->int:

        iniciativas = self.get_iniciativas_meta(cod_iniciativa)
        mapper = self.gen_iniciativas_mapper(iniciativas)
        codigo_limpo = self.clean_codigo(cod_iniciativa)

        return mapper[codigo_limpo]
    
    def __call__(self, cod_iniciativa:str)->int:

        return self.pipeline(cod_iniciativa)



