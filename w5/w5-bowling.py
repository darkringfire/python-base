def main():
    n, k = tuple(map(int, input().split()))
    pins = 'I'*n
    for i in range(k):
        l, r = tuple(map(int, input().split()))
        pins = pins[:l-1] + '.'*(r-l+1) + pins[r:]
    print(pins)


main()
