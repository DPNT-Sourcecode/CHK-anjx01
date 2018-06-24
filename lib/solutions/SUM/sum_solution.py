

# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    try:
        if x or y not in range(101):
            return 'hello'

        return x+y
    except TypeError:
        print 'x or y are not integers'


