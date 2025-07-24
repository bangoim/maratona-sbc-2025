def main():
    n = int(input())
    if n == 0:
        return

    h = list(map(int, input().split()))
    picos = 0

    for i in range(n):
        prev = h[(i - 1) % n]
        curr = h[i]
        next = h[(i + 1) % n]

        if (curr > prev and curr > next) or (curr < prev and curr < next):
            picos += 1

    print(picos)




if __name__ == "__main__":
    while True:
        try:
            main()
        except EOFError:
            break
