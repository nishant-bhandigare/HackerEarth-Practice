test_cases = int(input())

for i in range(test_cases):
    input_list = input().split()
    num_rows, num_cols = int(input_list[0]), int(input_list[1])

    table = []

    for i in range(num_rows):
        table.append(input())

    count = 0
    maximum_border = 0

    for row in table:
        for i in range(num_cols-1):
            if row[i]=='#' and row[i+1]=='#':
                count += 1

        if maximum_border < count:
            maximum_border = count

        count = 0
        
    print(maximum_border+1)