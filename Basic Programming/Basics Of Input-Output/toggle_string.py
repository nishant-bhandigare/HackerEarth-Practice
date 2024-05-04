string = input()

for i in range(len(string)):
    if ord(string[i])>=65 and ord(string[i])<=90:
        string[i] = chr(ord(string[i]) + 32)
    elif ord(string[i])>=97 and ord(string[i])<=112:
        string[i] = chr(ord(string[i]) - 32)

print(string)
