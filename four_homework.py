def get_user_info() -> tuple[str, str, str]: 
            global exit_choice 

            global full_name
            full_name = input("Please, enter your full name (at least 2 symbols in each word): ")
            choice_initials = input("Show only initials? (y/n): ").lower()
            show_only_initials = choice_initials == 'y' 
            valid_name = validate_name(full_name, show_only_initials)

            global email
            email = input("Enter your email: ")
            choice_mask = input("Would you like to mask email? (y/n)").lower()
            mask_email = choice_mask == 'y'
            valid_email = validate_email(email, mask_email)

            global password 
            password = input("Enter yout password(at least 8 symbols): ")
            choice_encrypt = input("Would you like to encrypt password? (y/n)").lower()
            encrypt_paassword = choice_encrypt == 'y'
            valid_passwd = validate_password(password, encrypt_paassword)

            return valid_name, valid_email, valid_passwd



def validate_email(email: str, mask_email: bool) -> str:
    if not email.strip() or not email.endswith((".com", ".org")) or len(email) < 14 or email.count('@') > 1:
        print("Write your correct email: ")
    else:
        try:
            if mask_email:
                email, domain = email.split("@")
                masked_middle = '*' * (len(email) - 2)
                return f'{email[0]}{masked_middle}{email[-1]}@{domain}'
            else:
                return email
        except ValueError:
            print("invalid syntax for email")
            
    


def validate_password(password: str, encrypt_paassword: bool) -> str:
    try:
        if len(password) > 8 and encrypt_paassword:
            reversed_paassword = "".join(reversed(password))
            return f'Your encrypted password: {reversed_paassword}' #ОБОРОТНЕ ШИФРУВАННЯ(?)
        if len(password) > 8 and not encrypt_paassword:
            return password
    except ValueError:
        print("Too small symbols")


def validate_name(full_name: str, show_only_initials: bool) -> str:
    words_in_full_name = full_name.strip().split() 
    try:
        if len(words_in_full_name) >= 2 and len(words_in_full_name[0]) >= 2 and len(words_in_full_name[1]) >= 2:
            name_initials = " ".join([initials[0] for initials in words_in_full_name])
            if show_only_initials:
                return name_initials
            else:
                return full_name
    except ValueError:
        print("Ops, incorred data entered or your full name is too small. Try again\n")

def main() -> None:
    exit_choice = input("Welcome to progran!\n Would you want to start? (y/n)").lower()
    if exit_choice == 'y':
        user_data = get_user_info()
        print(f'here you are: {user_data}')
    else:
        print("Ok, bye! ")

main()