# social_media.py

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []
        self.likes = {}

    def add_post(self, content):
        """Add a new post."""
        post = Post(self.username, content)
        self.posts.append(post)
        print(f"Post added by {self.username}: {content}")
        return post

    def like_post(self, post):
        """Like a post."""
        if post not in self.likes:
            self.likes[post] = 1
            post.add_like(self.username)
            print(f"{self.username} liked the post.")
        else:
            print(f"{self.username} has already liked this post.")

class Post:
    def __init__(self, username, content):
        self.username = username
        self.content = content
        self.likes = []

    def add_like(self, username):
        """Add a like to the post."""
        if username not in self.likes:
            self.likes.append(username)
    
    def display(self):
        """Display the post details."""
        print(f"Post by {self.username}: {self.content}")
        print(f"Likes: {len(self.likes)}")

class SocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def register_user(self, username, email, password):
        """Register a new user."""
        if username in self.users:
            print(f"Username {username} already exists.")
        else:
            user = User(username, email, password)
            self.users[username] = user
            print(f"User {username} registered successfully.")
    
    def login_user(self, username, password):
        """Login a user."""
        if username in self.users:
            user = self.users[username]
            if user.password == password:
                print(f"User {username} logged in successfully.")
                return user
            else:
                print("Incorrect password.")
        else:
            print(f"User {username} not found.")
        return None

    def display_users(self):
        """Display all users."""
        print("Users Registered:")
        for username in self.users:
            print(f"- {username}")

def main():
    platform = SocialMediaPlatform()

    while True:
        print("\nSocial Media Platform")
        print("1. Register User")
        print("2. Login User")
        print("3. View Users")
        print("4. Add Post")
        print("5. Like Post")
        print("6. View Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            username = input("Enter username: ").strip()
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            platform.register_user(username, email, password)

        elif choice == '2':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            user = platform.login_user(username, password)

        elif choice == '3':
            platform.display_users()

        elif choice == '4':
            if 'user' in locals():
                content = input("Enter post content: ").strip()
                post = user.add_post(content)
            else:
                print("Please login first to add a post.")

        elif choice == '5':
            if 'user' in locals():
                post_username = input("Enter the username of the post owner: ").strip()
                if post_username in platform.users:
                    post = platform.users[post_username].posts[-1]  # Latest post
                    user.like_post(post)
                else:
                    print("User not found.")
            else:
                print("Please login first to like a post.")

        elif choice == '6':
            if 'user' in locals():
                for u in platform.users.values():
                    for post in u.posts:
                        post.display()
            else:
                print("Please login first to view posts.")

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
