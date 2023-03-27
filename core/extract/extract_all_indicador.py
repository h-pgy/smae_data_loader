from core.extract.extract_wb import ExtractWb
from core.config import ORIGINAL_DATA_FOLDER
from core.utils.path import solve_dir, solve_path, lst_files
from typing import Generator

class ExtractAll:
    
    
    def __init__(self, data_folder:str=ORIGINAL_DATA_FOLDER):
        
        self.data_folder = data_folder
        self.extract_data = ExtractWb()
    
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