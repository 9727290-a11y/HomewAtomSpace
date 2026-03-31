#task1
full_name = input("Please, enter your name and surname: ")
initial_name = " ".join([initials[0] for initials in full_name.split()])

while not full_name.strip():
    full_name = input("Please, enter your correct name and surname: ")
    initial_name = " ".join([initials[0] for initials in full_name.s[lit()]])
else:
        print(f'Your name and surname initials: {initial_name}')

#tsk2
user_email = input("Please, enter your email: ")
if not user_email.strip() or not user_email.endwith((".com", ".org")):
    user_email = input("Please, enter your correct email: ")
else:
    username, domain = user_email.split("@")
    masked_middle = '*' * (len(username) - 2)
    print(f'{username[0]}{masked_middle}{username[-1]@{domain}}')

#tsk3
user_add_num = int(input("What num would you like to add? "))
list_of_num = [1,2,3,4,5]
if user_add_num in list_of_num:
    print(list_of_num)
else:
    print(list_of_num + [user_add_num])

#tsk4
first_user_tags = set()
second_user_tags = set()
#set() - створює список

first_user_input_tags = input("User1: Enter what you are interested in: ").strip().split(",")
second_user_input_tags = input("User2: Enter what you are interested in: ").strip().split(",")
first_user_tags.update(first_user_input_tags)
second_user_tags.update(second_user_input_tags)
common_tags = first_user_tags.intersection(second_user_tags) 
all_unique_tags = first_user_tags.union(second_user_tags)

if len(first_user_input_tags) == 3 and len(second_user_input_tags) == 3:
    print("Intersection of two users: " + ", ".join(common_tags))
    print("Union: " + ", ".join(all_unique_tags))
elif len(first_user_input_tags) != 3 or len(second_user_input_tags) != 3:
    print("Error. Write tags")
    first_user_input_tags = input("User1: Enter what you are interested in: ").strip().split(",")
    second_user_input_tags = input("User2: Enter what you are interested in: ").strip().split(",")
    
#.intersection() - метод, який шукає спільне з двох списків
#.union() - метод, який шукає що не повторювалось з двох списків
#.join() - поєднує список слів в один або розділяє, можна додати сепаратор


#tsk5

while True:

    user_num_input = input("Enter a three num with backspaces: ").split()

    try:
        if len(user_num_input) != 3:
            raise ValueError("You wrote more or less than three num")

        list_for_user_num = []

        for num in user_num_input:
            convert_num_to_float = float(num)
            list_for_user_num.append(convert_num_to_float)

        sum_of_num = sum(list_for_user_num)
        print(f'Your sum of three numbers: {sum_of_num}')
        break

    except ValueError:
        print("Error adding numbers: You must enter three numbers, and they must be valid")

#sum() - рахує суму введених чисел, які були записані у список
'''
  try: перевірка якщо користувач ввів все правильно, якщо ні перекине в except
    raise - створює виняток ValueError - перекине в except, якщо 
    правильний тип даних і не те значення + якщо користувач ввів не 3 цифри
        except виконається коли не виконаються умови в тру
'''