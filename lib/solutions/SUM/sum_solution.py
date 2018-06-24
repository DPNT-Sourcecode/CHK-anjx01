

# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    try:
        if (x or y) not in range(101):
            raise ValueError
        if not isinstance(x,int) or not isinstance(y,int):
            raise TypeError
        else:
            return x+y
    except TypeError as e:
        raise e
        print '{}: x or y are not integers'.format(e)
    except ValueError as e:
        raise e
        print '{}: x or y out of range 0-100'.format(e)


if __name__ == '__main__':
    print compute(1,1.1)
