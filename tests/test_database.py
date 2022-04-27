import unittest


class DatabaseTest(unittest.TestCase):

    def setUp(self):
        self.discounts = [
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
                "sku": "ipd",
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

        self.products = {
            "ipd": ["Super iPad", 549.99],
            "mbp": ["MacBook Pro", 1399.99],
            "atv": ["Apple TV", 109.50],
            "vga": ["VGA adapter", 30.00]
        }

        self.input = ["atv", "ipd", "ipd", "atv", "ipd", "ipd", "ipd"]