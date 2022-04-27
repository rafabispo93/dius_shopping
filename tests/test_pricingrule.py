from app.pricingrule import PricingRule
from tests.test_database import DatabaseTest


class PricingRuleTest(DatabaseTest):
    def test_bad_sku_key(self):
        bad_discounts = [
            {
                "sku": "atv",
                "discount": 0,
                "number_products_activation": 3,
                "extra_products": [
                    {
                        "atv": 1
                    }
                ]
            },
            {
                "sku": "aaa",
                "discount": 499.99,
                "number_products_activation": 5,
                "extra_products": [
                ]
            },
            {
                "sku": "mbp",
                "discount": 0,
                "number_products_activation": 1,
                "extra_products": [
                    {
                        "vga": 1
                    }
                ]
            }
        ]
        with self.assertRaises(ValueError):
            for pr in bad_discounts:
                PricingRule(
                    sku=pr['sku'],
                    discount=pr['discount'],
                    number_products_activation=pr['number_products_activation'],
                    extra_products=pr['extra_products'],
                    products_available=self.products,
                )

    def test_bad_sku_key_in_extra_products(self):
        bad_discounts = [
            {
                "sku": "atv",
                "discount": 0,
                "number_products_activation": 3,
                "extra_products": [
                    {
                        "atv": 1
                    }
                ]
            },
            {
                "sku": "atv",
                "discount": 499.99,
                "number_products_activation": 5,
                "extra_products": [
                ]
            },
            {
                "sku": "mbp",
                "discount": 0,
                "number_products_activation": 1,
                "extra_products": [
                    {
                        "error": 1
                    }
                ]
            }
        ]
        with self.assertRaises(ValueError):
            for pr in bad_discounts:
                PricingRule(
                    sku=pr['sku'],
                    discount=pr['discount'],
                    number_products_activation=pr['number_products_activation'],
                    extra_products=pr['extra_products'],
                    products_available=self.products,
                )