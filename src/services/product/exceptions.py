class NoBalanceError(Exception):
    message: str = "Lack of funds on the balance sheet"


class ProductNotFound(Exception):
    message: str = "Product not found"


class InsufficientQuantityStock(Exception):
    message: str = "Insufficient quantity stock a product"
