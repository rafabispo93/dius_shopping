class PricingRule:
    def __init__(
            self,
            sku: str,
            number_products_activation: int,
            discount: int,
            extra_products: list[dict[str, int]] = [],
            products_available: dict[str, list[str, float]] = {},
    ):
        if not sku in products_available.keys() and products_available:
            raise ValueError(f'Invalid sku {sku}')
        if not any(set(ep.keys()).intersection(set(products_available.keys())) for ep in extra_products) and extra_products:
            raise ValueError('Invalid sku in extra_products')

        self.sku = sku
        self.number_products_activation = number_products_activation
        self.discount = discount
        self.extra_products = extra_products

