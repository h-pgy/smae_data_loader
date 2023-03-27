

def mes_to_int(mes:str)->int:

    mes = mes.lower().strip()

    mapper = {
        'dezembro' : 12,
        'novembro' : 11,
        'outubro' : 10,
        'setembro' : 9,
        'agosto' : 8,
        'julho' : 7,
        'junho' : 6,
        'maio' : 5,
        'abril' : 4,
        'março' : 3,
        'marco' : 3,
        'fevereiro' : 2,
        'janeiro' : 1
    }

    return mapper[mes]