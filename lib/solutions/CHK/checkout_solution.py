

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count = {}
    for char in skus:
        if char not in ['ABCD']:
            return -1
