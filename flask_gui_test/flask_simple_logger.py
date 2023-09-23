

class FlaskSimpleLogger():
    def __init__(self) -> None:
        self.NEW_LINE = '\n'
        self.log = []
    
    def add(self, value):
        self.log.append(str(value))
    
    def clear(self):
        self.log = []
    
    def get_log_str(self):
        ret = ''
        for val in self.log:
            ret += val + self.NEW_LINE
        return ret