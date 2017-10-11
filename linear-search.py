foo = [1, 6, 5, 8, 7, 2, 3]


def search(arr, item):
    for i in foo:
        if i == item:
            return True
    return False


print(search(foo, 2))
print(search(foo, 20))
