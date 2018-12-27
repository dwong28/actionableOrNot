def is_actionable(num):
    error_dict = {
        '04043': 'Non-Actionable',
        '04080': 'Non-Actionable',
        '02261': 'Non-Actionable',
        '02437': 'Non-Actionable',
        '02260': 'Non-Actionable',
        '02441': 'Non-Actionable',
        '02442': 'Non-Actionable',
        '02443': 'Non-Actionable',
        '02275': 'Non-Actionable',
        '01440': 'Non-Actionable',
        '01451': 'Non-Actionable',
        '01408': 'Non-Actionable',
        '01418': 'Non-Actionable',
        '01430': 'Non-Actionable',
        '00904': 'Non-Actionable',
        '00955': 'Non-Actionable',
        '00942': 'Non-Actionable',
        '01758': 'Non-Actionable',
        '00001': 'Non-Actionable',
        '00060': 'Non-Actionable',
        '00273': 'Non-Actionable',
        '00957': 'Non-Actionable',
        '00972': 'Non-Actionable',
        '01442': 'Non-Actionable',
        '01917': 'Non-Actionable',
        '02264': 'Non-Actionable',
        '02273': 'Non-Actionable',
        '02291': 'Non-Actionable',
        '02429': 'Non-Actionable',
        '04095': 'Non-Actionable',
        '27477': 'Non-Actionable',
        '20500': 'Non-Actionable',
        '22859': 'Non-Actionable',
        '01562': 'Actionable',
        '04088': 'Actionable',
        '04068': 'Actionable',
        '04061': 'Actionable',
        '04065': 'Actionable',
        '06508': 'Actionable',
        '06512': 'Actionable',
        '06550': 'Actionable',
        '01452': 'Actionable',
        '01400': 'Actionable',
        '04063': 'Actionable',
        '04098': 'Actionable',
        '06502': 'Actionable',
        '12899': 'Actionable',
        '00936': 'Actionable',
        '30036': 'Actionable',
        '01652': 'Actionable',
        '00054': 'Actionable'
    }
    if num in error_dict:
        return error_dict[num]
    else:
        return "new or otherwise unlisted error. Check CRM for how to process."


def test_input(input):
    if input == '':
        return 'exit'
    if input[:3] == 'ORA' or input[:3] == 'ora':
        # Input Tests if User Input starts with 'ORA' or 'ora'
        if len(input) != 9:
            # If the input starts with 'ora' but doesn't have the right length
            return -1
        else:

            try:
                # If input has the right length, but the last 5 characters don't make an int
                test_num = int(input[4:])
                if test_num > 40322:
                    return -1
                else:
                    return 1
            except ValueError:
                return -1
    else:
        # Input Tests if User Input does not include 'ORA-' or 'ora-'
        if len(input) != 5:
            return -1
        else:
            try:
                # If input length is 5 but does not make a number
                test_num = int(input)
                if test_num > 40322:
                    return -1
                else:
                    return 1
            except ValueError:
                return -1


print("Welcome to the Actionable or Not Tool")
user_input = 'y'
while user_input != '':
    user_input = input("Please enter the Oracle Error code (Press Enter to Exit): ")
    if test_input(user_input) == 'exit':
        print("Exiting")
    elif test_input(user_input) == 1:
        if user_input[:3] == 'ORA' or user_input[:3] == 'ora':
            action = is_actionable(user_input[4:])
            print("Oracle Error " + user_input + " is a " + action + " error.")
        else:
            action = is_actionable(user_input)
            print("Oracle Error ORA-" + user_input + " is a " + action + " error.")
    else:
        print("Error 0001: Invalid Entry. Please revise your answer.")