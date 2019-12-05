LOWER_LIMIT = 264360
UPPER_LIMIT = 746325

def passwordCountBruteForce(part):
    password_count = 0
    for num in range(LOWER_LIMIT, UPPER_LIMIT+1):
        num_str = str(num)
        if part == 1:
            if increasingNumber(num_str) and repeatingConsecutiveDigit(num_str):
                password_count += 1
        elif part == 2:
            if increasingNumber(num_str) and repeatingConsecutiveDigit_2(num_str):
                password_count += 1
    return password_count

def increasingNumber(num_str):
    return (''.join(sorted(num_str)) == num_str)

def repeatingConsecutiveDigit(num_str):
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            return True
    return False

def repeatingConsecutiveDigit_2(num_str):
    i = 0
    while i < len(num_str) - 1:
        j = i
        while j < len(num_str) - 1:
            if num_str[j] == num_str[j + 1]:
                j += 1
            else:
                break
        if j - i == 1:
            return True
        i = j + 1
    return False

def main():
    password_count = passwordCountBruteForce(1)
    print(f'There are {password_count} possible passwords.')
    password_count_2 = passwordCountBruteForce(2)
    print(f'After the extra detail, there are {password_count_2} possible passwords.')

if __name__ == '__main__':
    main()
