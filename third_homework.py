
while True:
    first_num = int(input("Enter your first number: "))
    second_num = int(input("Enter your second number: "))
    arithmetic_operation = input("Enter what operation you want to do (+, -, *, /) : ")
    if arithmetic_operation == "+":
        print(f'{first_num} + {second_num} =  {first_num+second_num}')
    elif arithmetic_operation == "-":
        print(f'{first_num} - {second_num} = {first_num-second_num}')
    elif arithmetic_operation == "/" and second_num != 0:
        print(f'{first_num} / {second_num} = {first_num/second_num}')
    elif arithmetic_operation == "*":
        print(f'{first_num} * {second_num} = { first_num*second_num}')
    else:
        print("invalid syntax. the input is incorrect or unsupported. ")
        continue

    exit_choice = input("\nDo you want to continue? (y/n): ").lower()
    if exit_choice != 'y':
        print("Have a great day!")
        break
#tsk2

user_balance = int(input("Enter your current balance: "))
expenses = {}

while True:
    category = input("Choose category you spent money on or press q to exit: ").casefold()
    amount = int(input(f"Write how much you spent on {category}: "))
    if category and amount <= user_balance:
        expenses[category] = expenses.get(category, 0) + amount
        continue

    exit_choice = input("\nDo you want to continue? (y/n): ").lower()
    if exit_choice != 'y':
        print("Have a great day!")
        break