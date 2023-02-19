class BaseClass:
    def __init__(self, value):
        self.value = value

    def do_something(self):
        print(f"Doing something with value: {self.value}")

class SubClassA(BaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.name = "SubClassA"

    def do_something(self):
        print(f"Doing something in {self.name} with value: {self.value}")

class SubClassB(BaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.name = "SubClassB"

    def do_something(self):
        print(f"Doing something in {self.name} with value: {self.value}")

class MainClass:
    def __init__(self, value, mode):
        if mode == "A":
            self.base = SubClassA(value)
        elif mode == "B":
            self.base = SubClassB(value)
        else:
            self.base = BaseClass(value)

    def do_something(self):
        self.base.do_something()

# mode A の場合
main_class = MainClass(10, "A")
main_class.do_something()
# Output: Doing something in SubClassA with value: 10

# mode B の場合
main_class = MainClass(20, "B")
main_class.do_something()
# Output: Doing something in SubClassB with value: 20

# mode が A も B もない場合
main_class = MainClass(30, "C")
main_class.do_something()
# Output: Doing something with value: 30


print('type={}'.format(str(type(main_class))))