def custom_len(data: list) -> int:
    count = 0
    for item in data:
        if item is None:
            break
        count += 1
    return count


def add(data: list, obj) -> None:
    if custom_len(data) == len(data):
        raise IndexError
    data[custom_len(data)] = obj


    # старый вариант:
    # for i in range(len(data)):
    #     if data[i] is None:
    #         data[i] = obj
    #         return data
    # raise IndexError


def get(data: list, index: int):
    if index > custom_len(data) - 1:
        raise IndexError
    count = 0
    for item in data:
        if count == index:
            return item
        count += 1


def insert(data: list, obj, index: int):
    if custom_len(data) == len(data):
        raise IndexError
    for i in reversed(range(custom_len(data))):
        data[i + 1] = data[i]
        if i == index:
            break
    data[i] = obj


def delete(data: list, index: int):
    if data[index] is None or index not in range(len(data)):
        raise IndexError
    for i in range(custom_len(data) - 1):
        if i >= index:
            data[i] = data[i + 1]
    data[i + 1] = None


if __name__ == '__main__':
    # тестовые штуки
    test_list = [1, 2, 3, 4, 5, 6, None, None, None, None]
    add(test_list, 7)

    delete(test_list, 3)
    insert(test_list, "test", 2)

    print(test_list)
    print(get(test_list, 2))