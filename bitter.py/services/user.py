from database.storage import users, User

def create_user(user_name: str) -> bool:
    if any(character in SPECIAL_CHARACTERS for character in user_name):
        return False
    user: User = {
        'name' : user_name,
        'followers' : [],
        'following': [],
        'posts': [],
    }
    users[user_name] = user
    return True


def get_current_user() -> str:
    """
    This function for getting name from user

    Here we ask for a username and checks if it already exists
    If the username does not exist, a new user is created
    otherwise, it welcomes the user back
    """
    user_name = ""
    while not user_name:
        user_name = input(f"Your username: ").strip()
    if user_name not in users:
        create_user(user_name)
        print(f"Created a new user: {user_name}")
    else:
        print(f"Welcome back, @{user_name}")
    return user_name

def follow_user(current_user) -> bool:
    """
    Allows the current user to follow another user and updates both profiles.
    """
    target_follow = input("write the username you want to follow: ").strip()
    if target_follow not in users:
        print("This user does not exist, check the correctness of the user")
        return False
    if target_follow == current_user:
        print("You cannot folow yourself")
        return False
    if target_follow in users[current_user]["following"]:
        print(f"You already follow this guy @{target_follow}")
        return False
    users[current_user]['following'].append(target_follow)
    users[target_follow]['followers'].append(current_user)
    return True


def unfollow_user(current_user) -> bool:
    """
    Allows the current user to unfollow another user and updates both profiles.
    """
    target_unfollow = input("write the username you want to unfollow: ").strip()
    if target_unfollow not in users[current_user]["following"]:
        print(f"You don't follow @{target_unfollow}")
        return False
    if target_unfollow not in users:
        print("This user does not exist, check the correctness of the user")
        return False
    users[current_user]['following'].remove(target_unfollow)
    users[target_unfollow]['followers'].remove(current_user)
    return True

def user_followers(current_user):
    """
    Displays a list of users who are following the current user.
    """
    if not users[current_user]['followers']:
        print("You don't have followers yet")
    else: 
        print(f"Your followers: {users[current_user]['followers']}")


def user_following(current_user):
    """
    Displays a list of users whom the current user is following.
    """
    if not users[current_user]['following']:
        print("You don't have following yet")
    else: 
        print(f"You following: {users[current_user]['following']}")
    
_SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
