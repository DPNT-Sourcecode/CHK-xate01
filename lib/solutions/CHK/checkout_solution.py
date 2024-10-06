from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count = defaultdict(int)
    for char in skus:
        if char not in 'ABCDE':
            return -1
        sku_count[char] += 1
        
    sku_count_vals = sku_count.keys()
    checkout_value = 0
    for key, value in sku_count.items():
        if key == 'A':
            sets_of_five = value // 5
            remaining = value % 5
            sets_of_three = remaining // 3
            remaining %= 3

            checkout_value += (
                (sets_of_five * 200) +
                (sets_of_three * 130) +
                (remaining * 50)
            )
        elif key == 'B':
            sets_of_two = value // 2
            remaining = value % 2
            checkout_value += (
                (sets_of_two * 45) +
                (remaining * 30)
            )
        elif key == 'C':
            checkout_value += (value * 20)
        elif key == 'D':
            checkout_value += (value * 15)
        elif key == 'E':
            checkout_value += (value * 40)
            if 'B' in sku_count.keys():
                checkout_value -= 30
            
    return checkout_value


