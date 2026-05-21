social_network = {}

# Function to add a user
def add_user(user):
    if user not in social_network:
        social_network[user] = []
        print(f"{user} added successfully!")
    else:
        print("User already exists.")

# Function to add friendship
def add_friend(user1, user2):

    if user1 not in social_network:
        social_network[user1] = []

    if user2 not in social_network:
        social_network[user2] = []

    # Add friendship both ways
    if user2 not in social_network[user1]:
        social_network[user1].append(user2)

    if user1 not in social_network[user2]:
        social_network[user2].append(user1)

    print(f"Friendship added between {user1} and {user2}")

# Function to display network
def display_network():
    print("\n--- Social Network ---")

    for user in social_network:
        print(f"{user} -> {social_network[user]}")

# Function to recommend friends
def recommend_friends(user):

    if user not in social_network:
        print("User not found.")
        return

    recommendations = {}

    # Friends of current user
    friends = social_network[user]

    # Find friends of friends
    for friend in friends:

        for mutual_friend in social_network[friend]:

            # Skip if same user
            if mutual_friend == user:
                continue

            # Skip existing friends
            if mutual_friend in friends:
                continue

            # Count mutual friends
            if mutual_friend not in recommendations:
                recommendations[mutual_friend] = 1
            else:
                recommendations[mutual_friend] += 1

    # Display recommendations
    print(f"\nFriend Recommendations for {user}:")

    if len(recommendations) == 0:
        print("No recommendations available.")
    else:
        for person in recommendations:
            print(f"{person} (Mutual Friends: {recommendations[person]})")

# Main menu
while True:

    print("\n===== SOCIAL NETWORK MENU =====")
    print("1. Add User")
    print("2. Add Friendship")
    print("3. Display Network")
    print("4. Recommend Friends")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':

        user = input("Enter username: ")
        add_user(user)

    elif choice == '2':

        user1 = input("Enter first user: ")
        user2 = input("Enter second user: ")

        add_friend(user1, user2)

    elif choice == '3':

        display_network()

    elif choice == '4':

        user = input("Enter username: ")
        recommend_friends(user)

    elif choice == '5':

        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Try again.")