

# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    try:
        if (x or y) not in range(101):
            return 'hello'
        else:
            return x+y
    except TypeError as e:
        raise e
        print '{}: x or y are not integers'.format(e)


if __name__ == '__main__':
    print compute(1,'2')
