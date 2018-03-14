from services.person_service import enter_a_friend, lookup_a_friend, show_all_friends


def main():
    friends = []
    running = True
    while running:
        print("\n\tContacts Manager")
        print("1) New Contact            2) Lookup")
        print("3) Show All                  4) End")
        option = input(">")
        if option == "1":
            friends.append(enter_a_friend())
        elif option == "2":
            lookup_a_friend(friends)
        elif option == "3":
            show_all_friends(friends)
        elif option == "4":
            running = False
        else:
            print("Unrecoginized Entry. Try Again")
    print("Program Ending")


if __name__ == "__main__":
    main()