

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_set = set(skus)
    if sku_set!={'A', 'B', 'C', 'D'}:
        return -1
    #raise NotImplementedError()


if __name__ == '__main__':
    print checkout('A')