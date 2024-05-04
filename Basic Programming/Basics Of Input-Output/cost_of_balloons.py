test_cases = int(input())
for i in range(test_cases):
    cost_green, cost_purple = [int(x) for x in input().split()]
    num_participants = int(input())

    cost_1 = 0
    cost_2 = 0
    for j in range(num_participants):
        solved_1, solved_2 = [int(x) for x in input().split()]
        cost_1 = cost_1 + solved_1*cost_green + solved_2*cost_purple
        cost_2 = cost_2 + solved_1*cost_purple + solved_2*cost_green

    min = cost_1 if cost_1 < cost_2 else cost_2

    print(min)