string = input().lower()
x = string.count('z')
y = string.count('o')

if 2*x == y:
    print("Yes")
else:
    print("No")