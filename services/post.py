from database.storage import users, posts, Post
from services.user import get_current_user

def create_post(author: str, content: str) -> bool:
    '''
    This function for creating post

    Checks if the author exists in the database, then validates the content.
    Returns True if successful, False otherwise.
    '''
    if author not in users:
        return False
    if not _validate(content):
        return False
    post_id = 1
    if posts:
        post_id = posts[-1]["id"] +1
    post: Post = {
        "id": post_id,
        "author": author,
        "content": content,
        "likes": [],
        "comments": [],
        "views": 0
    }
    posts.append(post)
    users[author]["posts"].append(post_id)
    return True

list_of_forbidden_words = ["pytin", "apple", "banana"]

def _validate(content: str) -> bool:
    '''
    This function used to validate the name

    This function checks if the content is not empty, does not exceed the maximum length,
    and contains no forbidden words
    '''
    if not content:
        return False
    if len(content) > _MAX_CONTENT_LENGTH:
        return False
    for word in list_of_forbidden_words:
        if word in content.lower():
            return False
    return True

_MAX_CONTENT_LENGTH = 250

def delete_post(current_user) -> bool:
    '''
    This function for deliting user's post

    This function verifies if the current user has permission to delete a specific post
    It iterates through the posts, and if the post ID matches the target ID and the author
    matches the current user, the post is successfully deleted
    '''
    target_id = int(input("enter id for post deleting: "))
    for post in posts:
        if post["id"] == target_id:
            if post['author'] == current_user:
                posts.remove(post)
                users[current_user]["posts"].remove(target_id)
                return True
            else: return False
    return False

def find_post_by_author(current_user) -> bool:
    '''
    This function used to find post by author

    Here we checking if our user is in the dictionary, then go through our post dictionary
    and if find the user -> show the post to the console
    '''
    target_user = input("From which user you want to find posts?")
    if target_user in users:
        for post in posts:
            if post['author'] == target_user:
                print(f"{post['author']}: {post['content']}")
                return True
    return False

def edit_post(current_user) -> bool:
    '''
    This function for editing user's post

    This function verifies if the current user has permission to edit a specific post
    It iterates through the posts, and if the post ID matches the target ID and the author
    matches the current user, the post is successfully edited
    '''
    target_id = int(input("enter id for post editing: "))
    for post in posts:
        if post['id'] == target_id:
            if post['author'] == current_user:
                edit_post = input("enter new text for your post: ")
                post['content'] = edit_post
                return True
            else: return False
        return False