from core.extract.extract_wb import ExtractWb
from core.config import ORIGINAL_DATA_FOLDER
from core.utils.path import solve_dir, solve_path, lst_files
from typing import Generator

class ExtractAll:
    
    og_data_folder = ORIGINAL_DATA_FOLDER
    
    def __init__(self, data_folder:str):
        
        self.data_folder = self.__solve_folder(data_folder)
        self.extract_data = ExtractWb()
        
    def __solve_folder(self, folder:str)->str:
        
        return solve_path(folder, self.og_data_folder)
    
    def __query_files(self, extensions:list, folder:str=None)->list:
        
        folder = folder or self.data_folder
        
        return lst_files(folder, extensions)
    
    @property
    def xl_files(self):
        
        xls = self.__query_files(['.xlsx', '.xls'])
        
        return [file for file in xls if 'Monitoramento Fisico'
               in file]

    
    def extract_all_files(self)->Generator[list, list, list]:
        
        for file in self.xl_files:
            data = self.extract_data(file)
            yield data
            
    def __call__(self)->Generator[list, list, list]:
        
        return self.extract_all_files()