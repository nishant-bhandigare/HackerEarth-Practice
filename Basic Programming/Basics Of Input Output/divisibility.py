N = int(input())
data = [int(x) for x in input().split()]

last_digits = []
for num in data:
    last_digits.append(num%10)
last_digits.reverse()

multiplier = 1
sum = 0

for num in last_digits:
    sum = sum + num*multiplier
    multiplier = multiplier*10

if sum%10 == 0:
    ans = "Yes"
else:
    ans = "No"

print(ans)