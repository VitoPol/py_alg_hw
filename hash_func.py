dict_ = {}


def get_hash(obj):
    hash_value = 0
    for i in obj:
        hash_value = ((hash_value + ord(i)) * ord(i) ** 10)

    return int(str(hash_value)[:4])


def add(obj):
    hash_value = get_hash(obj)
    try:
        dict_[hash_value].add(obj)
    except:
        dict_[hash_value] = {obj}


if __name__ == '__main__':
    add("яблоко")
    add("апельсин")
    add("банан")
    add("яблоко")
    add("грейпфрут")
    add("слива")
    add("киви")
    add("арбуз")
    add("яблоко")
    add("ягода")

    add("яблоко")
    add("грейпфрут")
    add("арбуз")
    add("test")

    print(dict_)
