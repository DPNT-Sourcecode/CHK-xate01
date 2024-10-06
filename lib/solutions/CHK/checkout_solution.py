from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count = defaultdict(int)
    for char in skus:
        if char not in 'ABCDEF':
            return -1
        sku_count[char] += 1
        
    checkout_value = 0
    for key in sorted(sku_count.keys())[::-1]:
        if key == 'A':
            sets_of_five = sku_count[key] // 5
            remaining = sku_count[key] % 5
            sets_of_three = remaining // 3
            remaining %= 3
            checkout_value += (
                (sets_of_five * 200) +
                (sets_of_three * 130) +
                (remaining * 50)
            )
        elif key == 'B':
            sets_of_two = sku_count[key] // 2
            remaining = sku_count[key] % 2
            checkout_value += (
                (sets_of_two * 45) +
                (remaining * 30)
            )
        elif key == 'C':
            checkout_value += sku_count[key] * 20
        elif key == 'D':
            checkout_value += sku_count[key] * 15
        elif key == 'E':
            checkout_value += sku_count[key] * 40
            if 'B' in sku_count.keys() and sku_count[key] >= 2:
                for _ in range(sku_count[key] // 2):
                    sku_count['B'] -= 1
        elif key == 'F':
            sets_of_three = sku_count[key] // 3
            for _ in range(sets_of_three):
                sku_count['F'] -= 1
            checkout_value += sku_count[key] * 10
            
    return checkout_value
