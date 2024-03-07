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

#dictionary()



person1 = {'09:00', '10:30', '11:30', '12:00', '13:00', '14:30'}
person2 = {'09:30', '10:00', '10:30', '12:00', '14:30', '16:00'}
person3 = {'09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00'}
person4 = {'11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00'}
# Available Times: '12:00' and '14:30'


def perfect_time(*args):
    available = args[0]
    for arg in args:
        available = available.intersection(arg)
    print(f"The best time to meet is {available}")      

perfect_time(person1, person2, person3, person4)