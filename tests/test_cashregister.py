from app.cashregister import CashRegister
from app.pricingrule import PricingRule
from tests.test_database import DatabaseTest


class CashRegisterTest(DatabaseTest):

    def test_scan(self):
        register = CashRegister(self.discounts, self.products)
        for prod in self.input:
            register.scan(prod)

        expected_result = {'atv': [219.0, 2], 'ipd': [2749.95, 5]}
        self.assertEqual(expected_result, register.get_scanned_products())

    def test_total(self):
        discounts = [
            PricingRule(
                sku=pr['sku'],
                discount=pr['discount'],
                number_products_activation=pr['number_products_activation'],
                extra_products=pr['extra_products'],
                products_available=self.products,
            ) for pr in self.discounts
        ]
        register = CashRegister(discounts, self.products)
        for prod in self.input:
            register.scan(prod)

        self.assertEqual(2718.95, register.total())
