from models.person import Person

def enter_a_friend():
    name = input("Enter Friend's Name:")
    phone = input("Enter Phone  Number:")
    email = input("Enter email Address:")
    return Person(name, phone, email)


def lookup_a_friend(friends):
    found = False
    name = input("Enter name for lookup:")
    for friend in friends:
        if name in friend.getName():
            print(friend)
            found = True

    if not found:
        print("No Friends match found")


def show_all_friends(friends):
    print("Showing all contacts:")
    for friend in friends:
        print(friend)
