from .extract_wb import ExtractWb as ExtractIndicadorData
from .extract_all_indicador import ExtractAll as ExtractAllIndicador

from .get_metas import GetMetas
from .get_iniciativas import GetIniciativas
from .get_indicador import GetIndicador

get_metas_api = GetMetas()
get_iniciativas_api = GetIniciativas()
get_indicadores_api = GetIndicador()


dados_indicador_gen = ExtractAllIndicador()