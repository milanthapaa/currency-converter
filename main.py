import requests
import pprint

realtime_exchange_rate = 'https://open.er-api.com/v6/latest/USD'


class RealTimeCurrencyConverter():
    """RealTimeCurrencyConverter"""

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        amount = amount

        if amount != 'USD':
            amount = amount / self.currencies[from_currency.upper()]

        amount = round(amount * self.currencies[to_currency.upper()], 4)

        return amount
