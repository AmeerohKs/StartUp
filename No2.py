N = int(input("Enter any number here: "))
for i in range(N):
    pattern = '+' * i + '=' + '+' * (N - i - 1)
    print(pattern)


