#task1
user_name_and_surname = input("Please, enter your name and surname: ")

while len(user_name_and_surname) == 0 or user_name_and_surname == " ":
    user_name_and_surname = input("Please, enter your correct name and surname: ")
else:
        print("Your name and surname: " + user_name_and_surname)

#tsk2
user_email = input("Please, enter your email: ")
if user_email == " " or len(user_email) == 0 or (".com" not in user_email and ".org" not in  user_email):
    user_email=input("Please, enter your correct email: ")
else:
    count_of_user_email = len(user_email)
    print("Your email: " + user_email.replace(user_email[1:-11], count_of_user_email * "*"))

#tsk3
user_add_num = int(input("What num would you like to add? "))
list_of_num = [1,2,3,4,5]
if user_add_num in list_of_num:
    print(list_of_num)
else:
    print(list_of_num + [user_add_num])

#tsk4
empty_set_user1 = set()
empty_set_user2 = set()
# сет() - створює список

user1_intrested_in = input("User1: Enter what you are interested in: ").strip().split(",")
user2_intrested_in = input("User2: Enter what you are interested in: ").strip().split(",")
empty_set_user1.update(user1_intrested_in)
empty_set_user2.update(user2_intrested_in)
users_intersection = empty_set_user1.intersection(empty_set_user2) 
users_union = empty_set_user1.union(empty_set_user2)

if len(user1_intrested_in) == 3 and len(user2_intrested_in) == 3:
    print("Intersection of two users: " + ", ".join(users_intersection))
    print("Union: " + ", ".join(users_union))
elif len(user1_intrested_in) != 3 or len(user2_intrested_in) != 3:
    print("Error. Write tags")
    user1_intrested_in = input("User1: Enter what you are interested in: ").strip().split(",")
    user2_intrested_in = input("User2: Enter what you are interested in: ").strip().split(",")
    
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
        print("Error")

    
#sum() - рахує суму введених чисел, які були записані у список
'''
  try: перевірка якщо користувач ввів все правильно, якщо ні перекине в except
    raise - створює виняток ValueError - перекине в except, якщо 
    правильний тип даних і не те значення + якщо користувач ввів не 3 цифри
        except виконається коли не виконаються умови в тру
'''