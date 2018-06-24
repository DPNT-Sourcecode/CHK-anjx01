

# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    try:
        return x+y
    except TypeError:
        raise NotImplementedError()

