a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

x, y = (d*e - b*f)/(a*d - b*c), (a*f - c*e)/(a*d - b*c)
print(x, y)
