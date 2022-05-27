import requests

realtime_exchange_rate = 'https://open.er-api.com/v6/latest/USD'


class RealTimeCurrencyConverter():
    """RealTimeCurrencyConverter"""

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
