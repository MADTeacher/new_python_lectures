class MyClass:
    def __init__(self, magic=3):
        self.magic = magic

    def square_magic(self):
        return self.magic ** 2

if __name__ == "__main__":
    my_test1 = MyClass()
    print(my_test1.square_magic()) # 9
    my_test2 = MyClass(5)
    print(my_test2.square_magic()) 
