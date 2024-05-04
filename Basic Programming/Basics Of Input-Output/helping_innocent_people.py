vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

def check(string):

    if string[2] in vowels:
        print("invalid")
        return
    elif (int(string[0]) + int(string[1]))%2 != 0 or (int(string[7]) + int(string[8]))%2 != 0:
        print("invalid")
        return
    else:
        for i in range(3,5):
            if (int(string[i]) + int(string[i+1]))%2 != 0:
                print("invalid")
                return

    print("valid")
    return


if __name__ == "__main__":
    string = input()
    check(string)