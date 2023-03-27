from openpyxl.worksheet.worksheet import Worksheet


class ExtractMetadata:


    @property
    def metadata_mapper(self):

        col = 'D'
        mapper = {
            'secretaria' : f'{col}5',
            'titulo' : f'{col}8',
            'direcao' : f'{col}9',
            'unidade_medida' : f'{col}10',
            'casas_decimais' : f'{col}11',
            'periodicidade' : f'{col}12',
            'regionalizavel' : f'{col}13',
            'atraso' : f'{col}14',
            'valor_base' : f'{col}15'
        }

        return mapper


    def parse(self, sheet:Worksheet)->dict:

        parsed = {}

        for col_name, cell_id in self.metadata_mapper.items():
            parsed[col_name] = sheet[cell_id].value

        return parsed

    def __call__(self, sheet:Worksheet)->dict:
        
        return self.parse(sheet)