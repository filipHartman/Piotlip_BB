
def max_in_list(list_name):
    list_name = sorted(list_name,reverse=True)
    largest_number_index = 0
    return list_name[largest_number_index]


def main():
    numbers = [1, 5, 3, 10, 2, 80, 45 ,584] 
    print(max_in_list(numbers))


if __name__ == "__main__":
    main()
