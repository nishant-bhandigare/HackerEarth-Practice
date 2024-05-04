match_count={0: 6,
             1: 2,
             2: 5,
             3: 5,
             4: 4,
             5: 5,
             6: 6,
             7: 3,
             8: 7,
             9: 6}

test_cases = int(input())

for _ in range(test_cases):

    num = input()
    total_matchsticks = 0

    # while True:
    #     r = num%10
    #     total_matchsticks = total_matchsticks + match_count[r]
    #     num = num//10
    #     if num == 0:
    #         break

    for digit in num:
        total_matchsticks = total_matchsticks + match_count[int(digit)]

    if total_matchsticks%2 == 0:
        for _ in range(total_matchsticks//2):
            print("1", end="")
    else:
        print("7", end = "")
        for _ in range((total_matchsticks-3)//2):
            print("1", end = "")
    
    print()