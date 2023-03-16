from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from openpyxl import load_workbook
import regex as re


from core.extract.data import DataExtractor
    
class ExtractWb:
    
    def __init__(self)->None:
        
        self.extract_data = DataExtractor()
    
    def read_wb(self, path:str)->Workbook:
        
        #tem que ser data only para nao puxar formula
        return load_workbook(path, data_only=True)
    
    def is_sheet_indicador(self, sheet_name:str)->bool:
        
        return sheet_name.lower().strip().endswith('indicador')
    
    def get_sheets_indicador(self):
        
        sheets = self.wb.get_sheet_names()
        
        return [sheet for sheet in sheets
               if self.is_sheet_indicador(sheet)]
    
    def extract_meta_iniciativa_cod(self, sheet_name:str)->str:
        
        try:
            meio = sheet_name.split(' ')[1]
            regex = '^\d+(\.[a-z])?'
        
            match = re.search(regex, meio)

            return match.group()
        
        except (IndexError, AttributeError):
            aviso = (f'Codigo meta ou iniciativa não encontrado na planilha:'
                    f' {sheet_name}')
            raise RuntimeError(aviso)
            
    def is_iniciativa(self, cod:str)->bool:
        
        regex = '\.[a-z]'
        match = re.search(regex, cod)
        
        if match:
            return True
        return False
            
    def open_sheet(self, sheet_name:str)->Worksheet:
        
        return self.wb[sheet_name]
    
    def add_values(self, row:dict, cod:str, is_iniciativa:bool, 
                   sheet_name:str)->None:
        
        row['codigo'] = cod
        row['is_iniciativa'] = is_iniciativa
        row['sheet_name'] = sheet_name
    
    def extract_sheet(self, sheet_name:str)->dict:
        
        sheet = self.open_sheet(sheet_name)
        data = self.extract_data(sheet)
        cod = self.extract_meta_iniciativa_cod(sheet_name)
        is_iniciativa = self.is_iniciativa(cod)
       
        for row in data:
            self.add_values(row, cod, is_iniciativa, sheet_name)
        
        return data
    
    def extract_sheets(self):
        
        sheets_indicador = self.get_sheets_indicador()
        all_data = []
        for sheet_name in sheets_indicador:
            data = self.extract_sheet(sheet_name)
            all_data.extend(data)
            
        return all_data
    
    def __call__(self, wb_path:str)->dict:
        
        self.wb = self.read_wb(wb_path)

        return self.extract_sheets()