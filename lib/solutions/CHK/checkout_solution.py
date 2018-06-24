

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_set = set(skus)
    if sku_set.difference((['A', 'B', 'C', 'D'])):
        return -1
    basket_count = {'A': 0, 'B': 0, 'C': 0, 'D':0}
    for letter in skus:
        basket_count[letter]+=1
    return basket_count



if __name__ == '__main__':
    print checkout('A')
