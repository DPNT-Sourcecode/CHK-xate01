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
        if key == 'A':
            sets_of_three = value // 3
            remaining = value % 3
            checkout_value += (
                (sets_of_three * 130) +
                (remaining * 50)
            )
