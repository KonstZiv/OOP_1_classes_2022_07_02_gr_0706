class ExampleObj:
    """Wry important class"""
    def __init__(self, param):
        self.param = param
    def __str__(self):
        """Return str representation for obj"""
        return f"exemplar of ExampleObj class, param = {self.param}"
    def __repr__(self):
        return f"====== exemplar of ExampleObj class, param = {self.param} ========"
    def __len__(self):
        return 20
    def __add__(self, other):
        """Return sum to obj"""
        return ExampleObj(self.param + other.param)
    def __bool__(self):
        return True if (0 < self.param < 10) else False