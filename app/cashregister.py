from app.pricingrule import PricingRule
from app.product import Product

PRODUCT_NAMES = {
    'ipd': 'Super iPad',
    'mbp': 'MacBook Pro',
    'atv': 'Apple TV',
    'vga': 'VGA adapter',
}


class CashRegister:
    def __init__(self, pricing_rules: list[PricingRule]):
        self.__pricing_rules = pricing_rules
        self.__products: dict[str, float] = {}

    def scan(self, product: Product) -> None:
        if product.sku not in self.__products:
            self.__products[product.sku] = product.price
        else:
            self.__products[product.sku] += product.price

    def total(self) -> float:
        total = 0.0
        self.__apply_discounts()
        for value in self.__products.values():
            total += value

        return total

    def __apply_discounts(self) -> None:
        for rule in self.__pricing_rules:
            if rule.sku in self.__products:
                self.__products[rule.sku] -= self.__products[rule.sku] * (rule.discount/100)
                for idx, extra in enumerate(rule.extra_products):
                    if rule.sku in extra:
                        product_unit_price = self.__products[rule.sku] / len(self.__products[rule.sku])
                        self.__products[rule.sku] -= product_unit_price * extra[rule.sku]
                    else:
                        for code, number in extra.items():
                            for _ in range(number):
                                self.scan(Product(
                                    sku=rule.sku,
                                    price=0.0,
                                    name=PRODUCT_NAMES[code]
                                ))