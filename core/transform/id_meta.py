from typing import Union

from core.extract import get_metas_api, dados_indicador_gen

class FindIdMeta:

    def __init__(self,metas_sistema:list=None)->None:

        self.metas = self.solve_metas(metas_sistema)
        self.metas_mapper = self.gen_meta_mapper(self.metas)

    def solve_metas(self, metas_sistema:Union[list, None])->list:

        if metas_sistema is None:
            metas_sistema = get_metas_api()
        
        return metas_sistema

    def clean_codigo(self, codigo:str)->str:
    
        if codigo.startswith('0'):
            codigo = codigo.lstrip('0')
        
        return codigo.rstrip().lower()
    
    def gen_meta_mapper(self, metas_api:list)->dict:
        
        mapper = {}
        for meta in metas_api:
            codigo = meta['codigo']
            codigo_limpo = self.clean_codigo(codigo)
            mapper[codigo_limpo] = meta['id']
            
        return mapper
    
    def add_codigo_limpo(self, meta_planilha:dict)->None:
        
        cod_original = meta_planilha['codigo']
        meta_planilha['codigo_limpo'] = self.clean_codigo(cod_original)

    def get_id_sistema(self, meta_planilha:dict)->dict:

        self.add_codigo_limpo(meta_planilha)

        codigo_limpo = meta_planilha['codigo_limpo']
        id_sistema = self.metas_mapper.get(codigo_limpo, 'nao_encontrado')

        meta_planilha['id_sistema'] = id_sistema

    
    def __call__(self, meta_planilha:dict):

        return self.get_id_sistema(meta_planilha)

    
    
