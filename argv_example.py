__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2019"
__email__ = "bilaleluneis@gmail.com"


def print_line(*messages: str):
    if not messages:
        print("no messages to print")
    else:
        for message in messages:
            print(message, end=" ")
        print()


def print_named_messages(**collection_of_messages):
    if not collection_of_messages:
        print("no named messages to print !")

    for messageName, messageText in collection_of_messages.items():
        if isinstance(messageName, str):
            print("string")
        if isinstance(messageName, int):
            print("int")
        print("{} is {}".format(messageName, messageText), end=" ")
        print()


my_dic = {1: "bilal", 2: "Jieshu"}


def main():
    print_line()
    print_line("messageOne")
    print_line("messageOne", "messageTwo")

    print()

    print_named_messages()
    print_named_messages(name="bilal", option2=30)

    # for key, _ in my_dic.items():
    #     print(type(key))

    print(type(list(my_dic.keys())[0]))


# start of running code
if __name__ == "__main__":
    main()
