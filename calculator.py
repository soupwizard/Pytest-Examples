
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
 
if __name__ == "__main__":

    # simple command line test of functions
    calc = Calculator()
    x = 4
    y = 5
    print("%2.2f + %2.2f = % 2.2f" % (x, y, calc.add(x,y)))
    print("%2.2f - %2.2f = % 2.2f" % (x, y, calc.subtract(x,y)))
    print("%2.2f * %2.2f = % 2.2f" % (x, y, calc.multiply(x,y)))
    print("%2.2f / %2.2f = % 2.2f" % (x, y, calc.divide(x,y)))
