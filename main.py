location_dict = {}  # Dictionary to store user locations

def create_account():
    username = input("Enter a username: ")
    confirmation = input(f"Are you sure you want '{username}' to be your username? (yes/no): ")

    if confirmation.lower() == "yes":
        with open("usernames.txt", "a") as file:
            file.write(username + "\n")
        print("Account created successfully!")
    else:
        print("Account creation canceled.")

def login():
    username = input("Enter your username: ")

    with open("usernames.txt", "r") as file:
        usernames = file.read().splitlines()

    if username in usernames:
        print("Login successful!")
        return username  # Return the logged-in username
    else:
        print("Login failed. Username not found.")
        return None  # Return None for failed login

def delete_user(username):
    global location_dict  # Access the global location_dict
    # Read the list of usernames from the text file
    with open("usernames.txt", "r") as file:
        usernames = file.read().splitlines()

    if username in usernames:
        # Remove the username from the list
        usernames.remove(username)

        # Write the updated list of usernames back to the text file
        with open("usernames.txt", "w") as file:
            for user in usernames:
                file.write(user + "\n")

        # Remove the user's location from the dictionary
        if username in location_dict:
            del location_dict[username]

        print(f"User '{username}' has been deleted.")
    else:
        print("User not found.")

def set_location(username):
    location = input("Enter the location for which you want to check the weather: ")
    location_dict[username] = location  # Store the location in the dictionary
    print(f"Location set to {location} for {username} for future weather checks.")

def view_locations(location_dict):
    if not location_dict:
        print("No locations have been set.")
    else:
        print("User Locations:")
        for username, location in location_dict.items():
            print(f"{username}: {location}")

def main():
    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            username = login()
            if username is not None:
                while True:
                    print(f"Logged in as {username}")
                    print("1. Set Location for Weather")
                    print("2. Settings")
                    print("3. View User Locations")
                    print("4. Logout")

                    user_choice = input("Enter your choice (1/2/3/4): ")

                    if user_choice == "1":
                        set_location(username)

                    elif user_choice == "2":
                        print("1. Change the degree measurement (Fahrenheit by Default)")
                        print("2. Delete Account")
                        print("3. Go Back")

                        user_choice = input("Enter your choice (1/2/3): ")

                        if user_choice == "1":
                            print("Implementation will be added later")

                        elif user_choice == "2":

                            confirmation = input(f"Are you sure you want to delete your account, '{username}'? (yes/no): ")

                            if confirmation.lower() == "yes":

                                delete_user(username)

                                print("Logged out.")

                                break
                            elif user_choice == "3":
                                print("Went back.")
                                break
                            else:
                                print("Invalid choice. Please select 1, 2, or 3.")

                    elif user_choice == "3":
                        view_locations(location_dict)
                    elif user_choice == "4":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Please select 1, 2, or 3.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
