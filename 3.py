s = int(input("Enter SUM of numbers: "))
p = int(input("Enter Multiply of numbers: "))

for x in range(1, s+1):
    if p % x == 0:
        y = p // x
        if x + y == s:
            print("Answer: ", x, y)
            break
else:
    print("It's not working!")