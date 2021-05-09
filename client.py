import json

from aiohttp import ClientSession


class Client:
    def __init__(self, base_api_url: str, session: ClientSession):
        self.api_url = base_api_url
        self._session = session

    async def get(self, endpoint, parse=False, **kwargs):
        async with self._session.get(self.api_url + endpoint, **kwargs) as response:
            content = await response.text()

            if parse:
                return self.parse_json(content)
            else:
                return content

    @staticmethod
    def parse_json(content):
        return json.loads(content)

    @staticmethod
    def json_to_string(obj):
        return json.dumps(obj)
