class MyList:
    def __init__(self, *args):
        self._data = list(args)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value


if __name__ == "__main__":
    my_list = MyList(1, 2, 3, 4, 5)
    print(my_list[2])  # 3
    my_list[2] = 10
    print(my_list[2])
