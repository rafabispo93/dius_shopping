from app.pricingrule import PricingRule


class CashRegister:
    def __init__(self, pricing_rules: list[PricingRule], products_available: dict[str, list[str, float]]):
        self.__pricing_rules = pricing_rules
        self.__products: dict[str, [float, int]] = {}
        self.products_available = products_available
        self.__discount_amount = 0

    def scan(self, product: str) -> None:
        price = self.products_available[product][1]
        if product not in self.__products:
            self.__products[product] = [price, 1]
        else:
            self.__products[product][0] += price
            self.__products[product][1] += 1

    def get_scanned_products(self):
        return self.__products

    def total(self) -> float:
        total = 0.0
        self.__apply_discounts()
        for value in self.__products.values():
            total += value[0]

        return total - self.__discount_amount

    def __apply_discounts(self) -> None:
        for rule in self.__pricing_rules:
            if rule.sku in self.__products:
                if self.__products[rule.sku][1] >= rule.number_products_activation:
                    self.__products[rule.sku][0] = self.__products[rule.sku][1] * rule.discount if rule.discount != 0 else self.__products[rule.sku][0]
                    for idx, extra in enumerate(rule.extra_products):
                        if rule.sku in extra:
                            product_unit_price = self.products_available[rule.sku][1]
                            self.__products[rule.sku][0] -= product_unit_price * extra[rule.sku]
                        else:
                            for code, number in extra.items():
                                for _ in range(number):
                                    if code in self.__products:
                                        self.__discount_amount += self.products_available[code][1]
