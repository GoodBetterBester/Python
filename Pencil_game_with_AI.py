names_list = ['John', 'Jack']
numbers = ['1', '2', '3']
AI_name = ' '
S_check_binary = 'false'
N_check_binary = 'false'
subt = int(77777)

def S_check(input1):
    while not input1.isnumeric():
        print('The number of pencils should be numeric')
        input1 = input()
    return int(input1)

def N_check(input2):
    while input2 < 1:
        input2 = input('The number of pencils should be positive')
        input2 = S_check(input2)
    return int(input2)

def PV_check(Possible_value):
    while Possible_value not in numbers:
        Possible_value = input('Possible values: \'1\', \'2\' or \'3\'')
    return int(Possible_value)

def TM_check(Too_many):
    while Too_many > pencils:
        Too_many = input('too many pencils')
        Too_many = PV_check(Too_many)
    return int(Too_many)

def Smart_bot():
    left = pencils
    if left == 1:
        choice = 1
        return choice
    elif left == 2:
        choice = 1
        return choice
    elif left == 3:
        choice = 2
        return choice
    elif left % 4 == 0:
        choice = 3
        return choice
    elif left % 4 == 0:
        choice = 3
        return choice
    elif left % 4 == 1:
        choice = 1
        return choice
    elif left % 4 == 2:
        choice = 1
        return choice
    elif left % 4 == 3:
        choice = 2
        return choice
    else:
       choice = 1
       return choice


pencils = input('How many pencils would you like to use: \n')
pencils = S_check(pencils)
pencils = N_check(pencils)

Current_player = input('Who will be the first (John, Jack): \n')
while Current_player not in names_list:
        Current_player = input('Choose between \'John\' and \'Jack\': \n')



loop_check = 1
while loop_check == 1:
    print ('|' * pencils)
    print(Current_player + "'s turn:")
    if Current_player == 'Jack':
        subt = Smart_bot()
        print(subt)
    else:
        subt = input()
        subt = PV_check(subt)
        subt = TM_check(subt)
    subt = int(subt)
    if Current_player == 'John':
            Current_player = 'Jack'
    else :
            Current_player = 'John'
    if pencils == subt:
        loop_check = 0
    else:

        pencils = pencils - subt
        loop_check = 1
print(Current_player + " won")
