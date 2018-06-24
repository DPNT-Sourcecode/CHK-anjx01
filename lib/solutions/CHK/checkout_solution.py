

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_set = set(skus)
    print sku_set
    if sku_set.difference((['A', 'B', 'C', 'D'])):
        return -1
    #raise NotImplementedError()


if __name__ == '__main__':
    print checkout('A')
