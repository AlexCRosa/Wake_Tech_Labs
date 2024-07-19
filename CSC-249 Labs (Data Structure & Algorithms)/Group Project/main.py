#
# Group: Smarty Pants
# 7/23/2024
#

""" This program is an info game for helping the
    user understand a few of data structures"""


def main():
    print("Welcome to the Data Structures info game!")

    response = ""

    while response != "0":
        display_main_menu()
        response = input('Enter your choice: ')

        if response == "1":
            from custom_array import Array, array_actions, display_array_info
            action_response = ""
            display_array_info()

            # Ask user for an initial length of the array
            capacity = int(input("How many initial elements do you want on the array? "))
            initial_array = Array(capacity)

            # Populate the array
            for item in range(capacity - 1, -1, -1):
                initial_array.insert(0, item)

            # Decided to create the initial array for not confusing the user
            print("An initial array was created.\n")
            print("Go ahead and modify the elements for better understanding. Happy studies!")
            print(f"Here is the initial array: {initial_array}")

            while action_response != "0":
                display_action_menu()
                action_response = input('Enter your choice: ')
                display_array_info(action_response)
                structure = array_actions(initial_array, action_response)

        elif response == "2":
            from listbag import ListBag, bag_actions, display_bag_info
            action_response = ""
            display_bag_info()

            initial_bag = ListBag()

            while action_response != "0":
                display_action_menu()
                action_response = input('Enter your choice: ')
                display_bag_info(action_response)
                structure = bag_actions(initial_bag, action_response)

        elif response == "3":
            from liststack import ListStack, stack_actions, display_stack_info
            action_response = ""
            display_stack_info()

            initial_stack = ListStack()

            while action_response != "0":
                display_action_menu()
                action_response = input('Enter your choice: ')
                display_stack_info(action_response)
                structure = stack_actions(initial_stack, action_response)

        elif response == "4":
            from listqueue import ListQueue, queue_actions
            action_response = ""

            initial_queue = ListQueue()

            while action_response != "0":
                display_action_menu()
                action_response = input('Enter your choice: ')
                structure = queue_actions(initial_queue, action_response)

        elif response != "0":
            print("Invalid choice. Try again.\n")

    print("\nThank you for playing the Data Structures info game!")


def display_main_menu():
    print("\nWhat type of data structure do you want to learn?")
    print("(1) Arrays\n"
          "(2) Bags\n"
          "(3) Stacks\n"
          "(4) Queues\n"
          "(0) Exit")


def display_action_menu():
    print("\nWhat action do you want to perform with the data structure you have chosen?")
    print("(1) Add an element\n"
          "(2) Remove an element\n"
          "(3) Check the structure length\n"
          "(4) Show elements of the structure\n"
          "(5) Clear the structure\n"
          "(0) Go back to the main menu")


if __name__ == '__main__':
    main()
