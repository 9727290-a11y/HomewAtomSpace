def get_user_info() -> tuple[str, str, str]:
    while True:
        full_name = input("Please, enter your full name (at least 2 symbols in each word): ")
        show_only_initials = input("Show only initials? (y/n): ").lower() == 'y'
        valid_name = validate_name(full_name, show_only_initials)
        if valid_name:
            break

    while True:
        email = input("Enter your email: ")
        mask_email = input("Would you like to mask email? (y/n)").lower() == 'y'
        valid_email = validate_email(email, mask_email)
        if valid_email:
            break

    while True:
        password = input("Enter yout password(at least 8 symbols): ")
        encrypt_paassword = input("Would you like to encrypt password? (y/n)").lower() == 'y'            
        valid_password = validate_password(password, encrypt_paassword)
        if valid_password:
            break

    return {"name": valid_name, "email": valid_email, "password": valid_password}

def validate_email(email: str, mask_email: bool) -> str:
        try:
            if not email.endswith((".com", ".org")) or len(email) < 14 or email.count('@') > 1:
                print("Write your correct email: ")
            else:
                if mask_email:
                    email, domain = email.split("@")
                    masked_middle = '*' * (len(email) - 2)
                    return f'{email[0]}{masked_middle}{email[-1]}@{domain}'
                else:
                    return email
        except ValueError:
            print("incorected data... ")           

def validate_password(password: str, encrypt_password: bool) -> str:
        try:
            if len(password) > 8:
                if encrypt_paassword:
                    reversed_paassword = "".join(reversed(password))
                    return f'Your encrypted password: {reversed_paassword}'
                else: 
                    return password[::1]
            else:
                print("Too small symbols")
        except ValueError:
            print("Incorrected data entered...")

def validate_name(full_name: str, show_only_initials: bool) -> str:
        name_parts = full_name.strip().split()
        try:
            if len(name_parts) >= 2 and len(name_parts[0]) >= 2 and len(name_parts[1]) >= 2:
                name_initials = " ".join([initials[0] for initials in name_parts])
                if show_only_initials:
                    return name_initials
                else:
                    return full_name
        except ValueError:
            print("Ops, incorred data entered or your full name is too small. Try again\n")

def main() -> None:
    exit_choice = input("Welcome to progran!\n Would you want to start? (y/n)").lower() == 'y'
    if exit_choice:
        user = get_user_info()
        print(f'{user["name"]}, \n{user["email"]}, \n{user["password"]}')
    else:
        print("Ok, bye! ")

main()
