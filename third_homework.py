#tsk1
user_exit = input(" press q if you wanna exit or any other symbol to start: ")
calculator_operation_existing = {
    "plus": "+",
    "minus": "-",
    "multiply": "*",
    "devide": "/",
}

while user_exit != "q":
    first_user_num = int(input("Enter your first number: "))
    second_user_num = int(input("Enter your second number: "))
    calculator_operation = input("Enter what operation you want to do (+, -, *, /) : ")
    if calculator_operation == "+":
        print(f'{first_user_num} + {second_user_num} =  {first_user_num+second_user_num}')
    elif calculator_operation == "-":
        print(f'{first_user_num} - {second_user_num} = {first_user_num-second_user_num}')
    elif calculator_operation == "/":
        print(f'{first_user_num} / {second_user_num} = {first_user_num/second_user_num}')
    elif calculator_operation == "*":
        print(f'{first_user_num} * {second_user_num} = { first_user_num*second_user_num}')
    elif calculator_operation not in calculator_operation_existing:
            print("invalid syntax. operation not existing yet. ")
            continue
    else:
        print("that was not an integer")
        continue

#tsk2

user_balance = int(input("Enter your current balance: "))
user_expanses_list = {
}

while user_exit != "q":
    expanses_category = input("Choose category you spent money on or press q to exit: ").casefold()
    amount_of_expanses = int(input(f"Write how much you spent on {expanses_category}: "))
    if expanses_category != 0 or "" and amount_of_expanses <= user_balance:
        user_expanses_list.update({expanses_category : amount_of_expanses})
        if user_balance > amount_of_expanses:
            user_balance = user_balance - amount_of_expanses
            print(f"Done! Your current balance: {user_balance}")
        elif user_balance < amount_of_expanses:
            print(f"sorry, insufficient funds for {expanses_category}")

            continue