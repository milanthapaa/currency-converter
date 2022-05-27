import requests

realtime_exchange_rate = 'https://open.er-api.com/v6/latest/USD'


class RealTimeCurrencyConverter():
    """RealTimeCurrencyConverter"""

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
        self.from_currency = input(
            "Add the currency abbreviations to convert from: ")
        self.to_currency = input(
            "Add the currency abbreviations to convert to: ")
        self.amount = int(input("Enter the amount to convert: "))
