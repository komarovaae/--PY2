# TODO Написать 3 класса с документацией и аннотацией типов


class P:
    def __init__(self, age, weight, name):
        self.age = age
        self.name = name
        self.weight = weight

        def read(self):
            print(f'{self.name} read')

            class Schoolboy(P):
                def __init__(self, mark, age, weight, name):
                    super().__init__(age, weight, name)
                    self.mark = mark



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    x = Schoolboy(5, 12, 35, name='Bob')
    y = Student(age=169, weight=90, name='Martin')
    q = Schoolboy(mark=4, age=15, weight=52, name='Tom')
    x.read()
    y.read()
    q.read()
    pass
