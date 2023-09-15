import requests as rq


class InfoController:
    def __init__(self, token, additional_headers=None):
        self.__token: str = token
        self.headers = {'Content-Type': 'application/json',
                        'Token': self.__token
                        }

        if additional_headers:
            self.headers.update(additional_headers)

    def info(self):
        url = 'https://datsorange.devteam.games/info'
        result = rq.get(url, headers=self.headers)
        return result.text
