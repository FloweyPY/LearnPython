def k(a, b):
    if a == b:
        return 1
    if a == 6:
        return 0
    if a == 12:
        return 0
    if a > b:
        return 0
    if a < b:
        return k(a + 1, b) + k(a + 3, b) + k(a * 2, b)
print(k(3, 16))
        