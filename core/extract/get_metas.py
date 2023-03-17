from core.api import API
from core.config import PDM_ID

class GetMetas:

    def __init__(self, api=None, pdm_id = PDM_ID):

        self.api = api or API()
        self.pdm_id = pdm_id

    def __call__(self):

        metas = self.api.get('meta', pdm_id=self.pdm_id)

        return metas.get('linhas', [])