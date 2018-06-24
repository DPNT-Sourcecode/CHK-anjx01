

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_set = set(skus)
    if sku_set.difference((['A', 'B', 'C', 'D'])):
        return -1
    basket_count = {'A': 0, 'B': 0, 'C': 0, 'D':0}
    for letter in skus:
        basket_count[letter]+=1

    total_val = 0
    price_model = {'A': {'single_pricing': 50, 'multi_num': 3, 'multi_pricing': 130},
                   'B': {'single_pricing': 30, 'multi_num': 2, 'multi_pricing': 45}, 
                   'C': 20,
                   'D': 15}
    for sku in basket_count:
        num_items = basket_count[sku]
        if len(price_model[sku])==3:
            total_val+= num_items/price_model['multi_num']*price_model['multi_pricing']+\
            num_items%price_model['multi_num']*price_model['single_pricing']




if __name__ == '__main__':
    print checkout('AAAAAAAAAABBBCCCCBBBDDD')
