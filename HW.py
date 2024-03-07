address_book = {}


def dictionary():
    while True:
        Question = input("What would you like to do ?").lower()
        if Question == 'quit':
            break
        elif Question == 'add':
            user_name = input("Please enter the name ")
            user_address = input("Please enter the address ")
            address_book[user_name] = user_address
        else:
            print("Invalid choice please speiy what would you like to do")
    

    for user_name in address_book:
        print(f"Here is your current adress book {address_book}")

dictionary()