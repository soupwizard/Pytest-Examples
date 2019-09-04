
class Calculator:

    def add(self, x, y):
        foo = x + y
        return foo

    def subtract(self, x, y):
        foo = x - y
        return foo

    def multiply(self, x, y):
        foo = x * y
        return foo

    def divide(self, x, y):
        # note: this function is incorrect on purpose so
        # that some tests will fail
        foo = x * y
        return foo

