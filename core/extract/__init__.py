from .extract_wb import ExtractWb as ExtractIndicadorData
from .extract_all_indicador import ExtractAll as ExtractAllIndicador

from .get_metas import GetMetas

get_metas_api = GetMetas()
dados_indicador_gen = ExtractAllIndicador()