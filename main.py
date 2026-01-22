import database
import sys

def print_menu():
    print("\n--- Registration System ---")
    print("1. Register User")
    print("2. List Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

def main():
    database.initialize_db()
    
    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            try:
                age = int(input("Age: "))
                database.add_user(name, email, age)
            except ValueError:
                print("Invalid age. Please enter a number.")

        elif choice == '2':
            users = database.get_users()
            if users:
                print("\nList of Users:")
                print(f"{'ID':<5} {'Name':<20} {'Email':<30} {'Age':<5}")
                print("-" * 60)
                for user in users:
                    print(f"{user[0]:<5} {user[1]:<20} {user[2]:<30} {user[3]:<5}")
            else:
                print("\nNo users registered.")

        elif choice == '3':
            try:
                user_id = int(input("ID of the user to update: "))
                name = input("New Name: ")
                email = input("New Email: ")
                age = int(input("New Age: "))
                database.update_user(user_id, name, email, age)
            except ValueError:
                print("Invalid input. ID and Age must be numbers.")

        elif choice == '4':
            try:
                user_id = int(input("ID of the user to delete: "))
                database.delete_user(user_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
