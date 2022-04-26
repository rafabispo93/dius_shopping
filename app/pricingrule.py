class PricingRule:
    def __init__(
            self,
            sku: str,
            number_products_activation: int,
            discount: int = 0,
            extra_products: list[dict[str, int]] = []
    ):
        self.sku = sku
        self.number_products_activation = number_products_activation
        if discount <= 100:
            self.discount = discount
        else:
            raise ValueError('Discount more than 100%')
        self.extra_products = extra_products

