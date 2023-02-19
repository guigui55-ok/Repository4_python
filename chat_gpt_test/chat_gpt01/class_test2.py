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
            self.__class__ = SubClassA
            self.__init__(value)
        elif mode == "B":
            self.__class__ = SubClassB
            self.__init__(value)
        else:
            self.base = BaseClass(value)

    def do_something(self):
        print(f"Doing something with value: {self.value}")

# mode A の場合
main_class = MainClass(10, "A")
print(type(main_class)) # Output: <class '__main__.SubClassA'>
main_class.do_something()
# Output: Doing something in SubClassA with value: 10

# mode B の場合
main_class = MainClass(20, "B")
print(type(main_class)) # Output: <class '__main__.SubClassB'>
main_class.do_something()
# Output: Doing something in SubClassB with value: 20

# mode が A も B もない場合
main_class = MainClass(30, "C")
print(type(main_class)) # Output: <class '__main__.MainClass'>
main_class.do_something()
# Output: Doing something with value: 30