class custom_adder(int):
    def __call__(self, v):
        return custom_adder(self + v)

def add(n):
    return custom_adder(n)
print(add(1)(2)(3))
