import random

class User:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests

class DatingApp:
    def __init__(self):
        self.users = []

    def add_user(self, name, age, interests):
        user = User(name, age, interests)
        self.users.append(user)
        print(f"{name} has been added to the dating app!")

    def list_users(self):
        for idx, user in enumerate(self.users, start=1):
            print(f"{idx}. Name: {user.name}, Age: {user.age}, Interests: {user.interests}")

    def match_users(self):
        if len(self.users) < 2:
            print("Not enough users to match.")
            return

        user1, user2 = random.sample(self.users, 2)
        print(f"Match: {user1.name} and {user2.name}!")

if __name__ == "__main__":
    dating_app = DatingApp()

    while True:
        print("\nDating App Menu:")
        print("1. Add User")
        print("2. List Users")
        print("3. Match Users")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            interests = input("Enter your interests: ")
            dating_app.add_user(name, age, interests)
        elif choice == "2":
            dating_app.list_users()
        elif choice == "3":
            dating_app.match_users()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
