from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count = defaultdict(int)
    for char in skus:
        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
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
        elif key == 'G':
            checkout_value += sku_count[key] * 20
        elif key == 'H':
            sets_of_ten = sku_count[key] // 10
            remaining = sku_count[key] % 10
            sets_of_five = remaining // 5
            remaining %= 5
            checkout_value += (
                (sets_of_ten * 80) +
                (sets_of_five * 45) +
                (remaining * 10)
            )
        elif key == 'I':
            checkout_value += sku_count[key] * 35
        elif key == 'J':
            checkout_value += sku_count[key] * 60
        elif key == 'K':
            sets_of_two = sku_count[key] // 2
            remaining = sku_count[key] % 2
            checkout_value += (
                (sets_of_two * 120) +
                (remaining * 70)
            )
        elif key == 'L':
            checkout_value += sku_count[key] * 90
        elif key == 'M':
            checkout_value += sku_count[key] * 15
        elif key == 'N':
            checkout_value += sku_count[key] * 40
            if 'M' in sku_count.keys() and sku_count[key] >= 3:
                for _ in range(sku_count[key] // 3):
                    sku_count['M'] -= 1
        elif key == 'O':
            checkout_value += sku_count[key] * 10
        elif key == 'P':
            sets_of_five = sku_count[key] // 5
            remaining = sku_count[key] % 5
            checkout_value += (
                (sets_of_five * 200) +
                (remaining * 50)
            )
        elif key == 'Q':
            sets_of_three = sku_count[key] // 3
            remaining = sku_count[key] % 3
            checkout_value += (
                (sets_of_three * 80) +
                (remaining * 30)
            )
        elif key == 'R':
            checkout_value += sku_count[key] * 50
            if 'Q' in sku_count.keys() and sku_count[key] >= 3:
                for _ in range(sku_count[key] // 3):
                    sku_count['Q'] -= 1
        elif key == 'U':
            sets_of_four = sku_count[key] // 4
            checkout_value += (sku_count[key] - sets_of_four) * 40
        elif key == 'V':
            sets_of_three = sku_count[key] // 3
            remaining = sku_count[key] % 3
            sets_of_two = remaining // 2
            remaining %= 2
            checkout_value += (
                (sets_of_three * 130) +
                (sets_of_two * 90) +
                (remaining * 50)
            )
        elif key == 'W':
            checkout_value += sku_count[key] * 20
            
    stxyz_group = sku_count['S'] + sku_count['T'] + sku_count['X'] + sku_count['Y'] + sku_count['Z']
    sets_of_three = stxyz_group // 3
    checkout_value += sets_of_three * 45
    
    for char in 'STXYZ':
        if char == 'S':
            checkout_value += sku_count[char] * 20
        elif char == 'T':
            checkout_value += sku_count[char] * 20
        elif char == 'X':
            checkout_value += sku_count[char] * 17
        elif char == 'Y':
            checkout_value += sku_count[char] * 20
        elif char == 'Z':
            checkout_value += sku_count[char] * 21
            
    return checkout_value






