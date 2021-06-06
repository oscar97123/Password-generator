import random


def password_gen(options_set, pw_length):
    password = ''
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-']
    similar_char = ['i', 'l', '1', '0', 'O']
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pw_options = [symbols, numbers, lower_case, upper_case, similar_char]
    choice = []
    exclude_sim_char_flag = False

    for option in options_set:
        # User chose "Exclude Similar Characters"
        if option == 4:
            exclude_sim_char_flag = True
        else:
            choice.append(pw_options[option])

    while len(password) < pw_length:
        random_option_digit = random.randint(0, len(choice)-1)
        random_value = random.randint(0, len(choice[random_option_digit])-1)
        if exclude_sim_char_flag:
            if choice[random_option_digit][random_value] in similar_char and similar_char in list(password):
                continue
        password += choice[random_option_digit][random_value]

    return password


def main():
    pw_length = None
    option = None
    options_set = set()

    print('Greeting!')

    # Ask for entering password length
    while True:
        try:
            pw_length = int(input('Please enter your prefer password length: '))
            break
        except ValueError:
            print('Please enter integer!!')
            continue

    print('Do you password have specify requirement?\n')
    print('Option 0: Symbols (@#$%)')
    print('Option 1: Include Numbers (123456)')
    print('Option 2: Include Lowercase Characters (abcdefgh)')
    print('Option 3: Include Uppercase Characters (ABCDEFGH)')
    print('Option 4: Exclude Similar Characters (i, l, 1, 0, O)')
    print('Please enter the option number: (-1 to end)')

    # Ask for entering password generate option(s)
    while option != -1:
        try:
            option = int(input())
            # Check if option is between -1 ~ 4
            assert -1 <= option <= 4
            options_set.add(option)
        except ValueError:
            print('Please enter integer / a single integer at one time!!')
        except AssertionError:
            print('Please enter an integer between -1 and 4')

    # Remove -1 from set
    options_set.remove(-1)

    if len(options_set) == 0:
        print('No options were inputted. Process exit.')
        exit(0)
    else:
        password = password_gen(options_set, pw_length)
        print('Your newly generated password: ', password)


main()
