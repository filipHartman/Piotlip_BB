
def max_in_list(list_name):
    list_name = sorted(list_name,reverse=True)
    largest_number_index = 0
    return list_name[largest_number_index]


def main():
    amount_of_elements = int(input("Enter amount of elements in list: "))
    numbers = list(range(amount_of_elements + 1))
    print(max_in_list(numbers))


if __name__ == "__main__":
    main()
