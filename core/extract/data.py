
from openpyxl.worksheet.worksheet import Worksheet


class DataExtractor:
        
        
    def is_ponto_partida(self, val:str)->bool:
        
        return 'ponto de partida' in str(val).lower().strip()
        
    
    def find_starting_point(self)->int:
        
        for cell in self.sheet['B']:
            val = cell.value
            if not val:
                continue
            if self.is_ponto_partida(val):
                return cell.row
            
    def find_last_row(self)->bool:
        
        count = 0
        for row in self.sheet.iter_rows():

            count+=1
            ano = str(row[2].value).lower()
            mes = str(row[3].value).lower()

            if '2024' in ano and 'dezembro' in mes:
                return count
    
    @property
    def column_mapper(self):
        
        mapper = {
            'C' : 'ano',
            'D' : 'mes',
            'E' : 'projetado_mensal',
            'F' : 'realizado_mensal',
            'G' : 'projetado_acumulado',
            'H' : 'realizado_acumulado'
        }
        
        return mapper
    
    def extract_row(self, i:int)->dict:
        
        return {col_name : self.sheet[f'{xl_col}{i}'].value 
               for xl_col, col_name in self.column_mapper.items()}
    
    def extract_rows(self)->dict:
        
        start = self.find_starting_point()
        end = self.find_last_row()
        
        data = []
        for i in range(start, end+1):
            mapped_row = self.extract_row(i)
            data.append(mapped_row)
        
        return data
    
    def __call__(self, sheet:Worksheet)->dict:
                
        self.sheet=sheet
        
        return self.extract_rows()