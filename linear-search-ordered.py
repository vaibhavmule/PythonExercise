foo = [1, 2, 3, 4, 6, 9, 10]


def search(arr, item):
    for i in arr:
        if i == item:
            return True
        elif i > item:
            return False
    return False


print(search(foo, 5))
print(search(foo, 9))
print(search(foo, 20))
