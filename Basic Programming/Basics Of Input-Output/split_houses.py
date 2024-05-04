n = int(input())
village = input()
flag = 1
for i in range(n-1):
    if village[i] == "H" and village[i+1] == "H":
        print("NO")
        flag = 0
        break

if flag:
    village = village.replace('.', 'B')
    print("YES")
    print(village)