a, b = int(input()), int(input())

ab, ba = a // b, b // a
print((a * ab + b * ba) // (ab + ba))
