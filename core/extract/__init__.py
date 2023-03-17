from .extract_wb import ExtractWb as ExtractIndicadorData
from .extract_all_indicador import ExtractAll as ExtractAllIndicador

from .get_metas import GetMetas
from .get_iniciativas import GetIniciativas

get_metas_api = GetMetas()
get_iniciativas_api = GetIniciativas()


dados_indicador_gen = ExtractAllIndicador()