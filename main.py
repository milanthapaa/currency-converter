import requests

realtime_exchange_rate = 'https://api.exchangerate-api.com/v4/latest/USD'


class RealTimeCurrencyConverter():
    """RealTimeCurrencyConverter"""

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
