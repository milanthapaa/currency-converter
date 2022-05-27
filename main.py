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

        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency.upper()]

        amount = round(amount * self.currencies[to_currency.upper()], 4)

        return amount


if __name__ == '__main__':
    # Instantiate currency converter class
    converter = RealTimeCurrencyConverter(realtime_exchange_rate)
    # pprint.pprint(converter.data)
    from_currencies = input("Insert the currency abbreviations (from): ")
    to_currencies = input("Insert the currency abbreviations (to): ")
    amounts = int(input("Insert the amount to convert: "))
    print(converter.convert(from_currencies, to_currencies, amounts))
