def main():
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        return

    start_minutes = x1 * 60 + y1
    end_minutes = x2 * 60 + y2

    if end_minutes <= start_minutes:
        end_minutes += 24 * 60

    print(end_minutes - start_minutes)

if __name__ == "__main__":
    while True:
        try:
            main()
        except EOFError:
            break
