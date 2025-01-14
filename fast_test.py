class test:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other


x = test(3) + 3 + 5

print(x)
