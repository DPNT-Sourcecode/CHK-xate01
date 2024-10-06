from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count = defaultdict(int)
    for char in skus:
        if char not in 'ABCD':
            return -1
        sku_count[char] += 1
        
    checkout_value = 0
    for key, value in sku_count.items():
        pass
