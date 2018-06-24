

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus)==list:
        skus = ''.join(skus)
    sku_set = set(skus)
    if sku_set.difference((['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])):
        return -1
    basket_count = {'A': 0, 'B': 0, 'C': 0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    for letter in skus:
        basket_count[letter]+=1

    total_val = 0
    price_model = {'A': [{'single_pricing': 50,'multi_num': 5, 'multi_pricing': 200, 'extra': None, 'extra_num': None}, 
                         {'single_pricing': 50, 'multi_num': 3, 'multi_pricing': 130, 'extra': None, 'extra_num': None}],
                   'B': {'single_pricing': 30, 'multi_num': 2, 'multi_pricing': 45, 'extra': None, 'extra_num': None}, 
                   'C': 20,
                   'D': 15,
                   'E': {'single_pricing': 40, 'multi_num':2, 'multi_pricing': 80, 'extra': 'B', 'extra_num': 1 },
                   'F': {'single_pricing': 10, 'multi_num':3, 'multi_pricing': 20, 'extra': None, 'extra_num': None },
                   'G': 20,
                   'H': [{'single_pricing': 10,'multi_num': 10, 'multi_pricing': 80, 'extra': None, 'extra_num': None}, 
                         {'single_pricing': 10, 'multi_num': 5, 'multi_pricing': 45, 'extra': None, 'extra_num': None}],
                   'I': 35,
                   'J': 60,
                   'K': {'single_pricing': 80, 'multi_num': 2, 'multi_pricing': 150, 'extra': None, 'extra_num': None},
                   'L': 90,
                   'M': 15,
                   'N': {'single_pricing': 40, 'multi_num':3, 'multi_pricing': 120, 'extra': 'M', 'extra_num': 1 },
                   'O': 10,
                   'P': {'single_pricing': 50, 'multi_num': 5, 'multi_pricing': 200, 'extra': None, 'extra_num': None},
                   'Q': {'single_pricing': 30, 'multi_num': 3, 'multi_pricing': 80, 'extra': None, 'extra_num': None},
                   'R': {'single_pricing': 50, 'multi_num': 3, 'multi_pricing': 150, 'extra': 'Q', 'extra_num': 1},
                   'S': 30,
                   'T': 20,
                   'U': {'single_pricing': 40, 'multi_num': 4, 'multi_pricing': 120, 'extra': None, 'extra_num': None},
                   'V': [{'single_pricing': 50,'multi_num': 3, 'multi_pricing': 130, 'extra': None, 'extra_num': None}, 
                         {'single_pricing': 50, 'multi_num': 2, 'multi_pricing': 90, 'extra': None, 'extra_num': None}],
                   'W': 20,
                   'X': 90,
                   'Y': 10,
                   'Z': 5  
                         
                         
                         
                         
                         }

    order = ['E','N', 'R' 'A','B','C','D','F']

    for sku in order:
        pricing = price_model[sku]
        if basket_count[sku]<0:
            basket_count[sku]=0
        if type(pricing)==dict:
            total_val+= basket_count[sku]/pricing['multi_num']*pricing['multi_pricing']+\
            basket_count[sku]%pricing['multi_num']*pricing['single_pricing']
            if pricing['extra']:

                basket_count[pricing['extra']]-= basket_count[sku]/pricing['multi_num']

        if type(pricing)==list:

            for price in pricing:

                total_val+= basket_count[sku]/price['multi_num']*price['multi_pricing']

                basket_count[sku]-=basket_count[sku]/price['multi_num']*price['multi_num']

            total_val+= basket_count[sku]*price['single_pricing']

        if type(pricing)==int:

            total_val+= basket_count[sku]*pricing
    return total_val

if __name__ == '__main__':
    print checkout('EE')
