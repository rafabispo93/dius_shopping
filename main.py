import json

from app.cashregister import CashRegister
from app.pricingrule import PricingRule

if __name__ == '__main__':
    with open('data/products.json') as products_file:
        try:
            products = json.load(products_file)
            products_file.close()
        except json.decoder.JSONDecodeError:
            raise Exception("Invalid JSON")

    with open('data/discounts.json') as discounts_file:
        try:
            discounts = json.load(discounts_file)
            discounts_file.close()
        except json.decoder.JSONDecodeError:
            raise Exception("Invalid JSON")

        discounts = [
            PricingRule(
                sku=pr['sku'],
                discount=pr['discount'],
                number_products_activation=pr['number_products_activation'],
                extra_products=pr['extra_products'],
                products_available=products
            ) for pr in discounts
        ]

        register = CashRegister(discounts, products)

    with open('data/input.json') as input_file:
        try:
            input_data = json.load(input_file)
            input_file.close()
        except json.decoder.JSONDecodeError:
            raise Exception("Invalid JSON")

        for input in input_data:
            print(input)
            register.scan(input)
        print(register.total())