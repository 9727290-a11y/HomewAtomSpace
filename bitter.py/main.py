from services.user import get_current_user
from services.post import create_post
from database.storage import posts, users
from services.post import find_post_by_author, delete_post, edit_post
from services.user import follow_user, unfollow_user, user_following, user_followers

def show_menu(current_user: str) -> None:
    """
    This main function show menu to user
    """
    print("\nWelcome to the bitter, where you can write posts!")
    print(f'You are signed as: {current_user}')
    print("1. Create post")
    print("2. Look at all posts")
    print("3. Find user's posts")
    print("4. Delete post with ID")
    print("5. Edit post")
    print("6. Follow user")
    print("7. Unfollow user")
    print("8. Show my follows/my following")
    print("9. Exit")

def main() -> None:
    '''
    TThe main execution loop and controller for the Bitter application

    It logs in the user, runs the main menu loop, and calls
    the appropriate functions based on the user's choice
    '''
    current_user = get_current_user()
    while True:
        show_menu(current_user)
        choice = input("What do you want to do? ").strip()
        if choice in ('1', 'create_post'):
            content = input("Write your post here: ").strip()
            if create_post(current_user, content):
                print("Your post was created")
            else:
                print("Could not create a post. Check the post length")
        elif choice in ('2', 'look at all posts'):
            for post in posts:
                if post["author"] != current_user:
                    post["views"]+=1
                formated_content = f"{post['author']}: {post['content']}"
                print(f"--------{post['author']}--------")
                print(f"{formated_content} \nviews: {post['views']}")
        elif choice in ('3', "find user's posts"):
            target_user = input("From which user you want to find posts? ")
            find_post_by_author(current_user, target_user)
            if post['author'] != current_user:
                post['views']+=1
            else: 
                print("there is no such user yet")
            print(f"views:{post['views']}")
        elif choice in ('4', "delete post with ID"):
            target_id = int(input("enter id for post deleting: "))
            if delete_post(current_user, target_id):
                print("Your post was delated")
            else: 
                print("you don't have access to this")
        elif choice in ('5', "edit post"):
            target_id = int(input("enter id for post editing: "))
            if edit_post(current_user, target_id):
                print("Your post editing successfull")
            else:
                print("you dont have access to this")
        elif choice in ('6', "follow user"):
            if follow_user(current_user):
                print("Follow successfull")
        elif choice in ('7', "unfollow user"):
            if unfollow_user(current_user):
                print("Unfollow successfull")
        elif choice in ('8', "show my followers/my following"):
            global followers_or_following
            followers_or_following = input("press 1 to see your followser and 2 to see your following: ")
            if followers_or_following == '1':
                user_followers(current_user)
            if followers_or_following == '2':
                user_following(current_user)
        elif choice in ('9', 'exit'):
            break

main()
