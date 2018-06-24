

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus)==list:
        skus = ''.join(skus)
    sku_set = set(skus)
    if sku_set.difference((['A', 'B', 'C', 'D'])):
        return -1
    basket_count = {'A': 0, 'B': 0, 'C': 0, 'D':0}
    for letter in skus:
        basket_count[letter]+=1

    total_val = 0
    price_model = {'A': {'single_pricing': 50,[{'multi_num': 5, 'multi_pricing': 200, 'extra': None, 'extra_num': None},
                                                {'multi_num': 3, 'multi_pricing': 130, 'extra': None, 'extra_num': None}]},
                   'B': {'single_pricing': 30, 'multi_num': 2, 'multi_pricing': 45, 'extra': None, 'extra_num': None}, 
                   'C': 20,
                   'D': 15,
                   'E': {'single_pricing': 40, {'multi_num':2, 'multi_pricing': 80, 'extra': 'B', 'extra_num': 1 }}}

    order = ['E','A','B','C','D']

    for sku in basket_count:
        pricing = price_model[sku]

        if type(pricing)==dict:
            total_val+= basket_count[sku]/pricing['multi_num']*pricing['multi_pricing']+\
            basket_count[sku]%pricing['multi_num']*pricing['single_pricing']
            if pricing['extra']:
                basket_count['extra']-= basket_count[sku]/pricing['multi_num']

        if type(pricing)==list:
            for price in pricing:
                pricing = price_model[sku]
                total_val+= basket_count[sku]/pricing['multi_num']*pricing['multi_pricing']
                basket_count[sku]-=basket_count[sku]/pricing['multi_num']
            total_val+= basket_count[sku]*pricing['multi']

        else:

            total_val+= num_items*pricing

    return total_val

if __name__ == '__main__':
    print checkout(['A'])
