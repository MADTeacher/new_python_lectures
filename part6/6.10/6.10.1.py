class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    my_list = MyList([1, 2, 3, 4])
    print(len(my_list)) # 4
