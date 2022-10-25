import os,json
from pathlib import Path
from typing import Optional

class GetHeaders:
    BASE_DIR = Path(__file__).resolve().parent

    @classmethod
    def get_headers(
            cls,
            key: str,
            default_value: Optional[str] = None
    ):
        JSON_FILE = os.path.join(cls.BASE_DIR,'headers.json')

        with open(JSON_FILE,'r',encoding='UTF-8') as file:
            headers = json.loads(file.read())

        try :
            return headers[key]
        except:
            if default_value:
                return default_value
            raise EnvironmentError(f'Set the {key}')
headers = GetHeaders()
