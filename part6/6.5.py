class MyClass:

    all_created_clases = []

    def __init__(self, magic=10):
        self.magic = magic
        MyClass.all_created_clases.append(self)
        #self.__class__.all_created_clases.append(self)

    def square_magic(self):
        """Возведение в квадрат"""
        return self.magic ** 2

    @staticmethod
    def sum_all_square_magic():
        rezult = 0
        for it in MyClass.all_created_clases:
            rezult += it.square_magic()
        return rezult

if __name__ == "__main__":
    my_test1 = MyClass()
    my_test2 = MyClass(5)
    my_test4 = MyClass(15)
    print(MyClass.sum_all_square_magic()) # 350
    my_test5 = MyClass(1)
    print(MyClass.sum_all_square_magic())
