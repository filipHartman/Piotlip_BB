def is_member(list_name, value):
    for element in list_name:
        if value == str(element):
            return True
    return False


def main():
    numbers = list(range(11))
    serched_item = input("Eneter a item to serch in list: ")
    print(is_member(numbers, serched_item))


if __name__ == "__main__":
    main()
