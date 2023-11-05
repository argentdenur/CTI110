x = int(input())
y = int(input())

if x > y:
    print("Second integer can't be less than the first.")
else:
    while x <= y:
        print(x, end=' ')
        x += 5
    print()