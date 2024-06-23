
class SampleLogger():
    def __init__(self) -> None:
        self.debug = True
    
    def info(self, value):
        if self.debug:
            print(value)