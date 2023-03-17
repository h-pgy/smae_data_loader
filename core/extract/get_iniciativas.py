from core.api import API
from core.config import PDM_ID

class GetIniciativas:

    def __init__(self):

        self.api = API()

    def __call__(self, meta_id:int)->list:

        metas = self.api.get('iniciativa', meta_id=meta_id)

        return metas.get('linhas', [])