import requests as rq
import json


class PlaceBidController:

    def __init__(self, token, additional_headers=None):
        self.__token: str = token
        self.headers = {'Content-Type': 'application/json',
                        'Token': self.__token
                        }

        if additional_headers:
            self.headers.update(additional_headers)

    def remove_bid(self, bid_id: int):
        url = 'https://datsorange.devteam.games/RemoveBid'

        payload = {
            'bidId': bid_id
        }
        result = rq.post(url, headers=self.headers, json=payload)
        return result.text

    def limit_price_sell(self, symbol_id: int, price: int, quantity: int):
        url = 'https://datsorange.devteam.games/LimitPriceSell'

        payload = {
            'symbolId': symbol_id,
            'price': price,
            'quantity': quantity,
        }
        result = rq.post(url, headers=self.headers, json=payload)
        return result

    def remove_bid(self, bid_id: int):
        url = 'https://datsorange.devteam.games/RemoveBid'

        payload = {
            'bidId': bid_id
        }
        result = rq.post(url, headers=self.headers, json=payload)
        return result

    def remove_bid(self, bid_id: int):
        url = 'https://datsorange.devteam.games/RemoveBid'

        payload = {
            'bidId': bid_id
        }
        result = rq.post(url, headers=self.headers, json=payload)
        return result

    def remove_bid(self, bid_id: int):
        url = 'https://datsorange.devteam.games/RemoveBid'

        payload = {
            'bidId': bid_id
        }
        result = rq.post(url, headers=self.headers, json=payload)
        return result