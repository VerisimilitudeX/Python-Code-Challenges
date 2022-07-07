def list_indexes(lst, item):
    indexes = []
    for i in range(len(lst)):
        if lst[i] == item:
            indexes.append(i)
    for index in indexes:
        print(index)

list_indexes(input("Enter the list that you want to search in: "), input("Enter the item you want to search for: "))