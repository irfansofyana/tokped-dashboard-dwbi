import random

def generate_fake_products():
    products = []
    
    #kategori & nama produk sementara dibuat manual dibawah
    category_type = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q']
    product_list_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS','TT','UU','VV','WW','XX','YY','ZZ']


    for produk in range(1000):
        name = product_list_name[random.randint(0, len(product_list_name)-1)]
        category = category_type[random.randint(0, len(category_type)-1)]
        price = random.randint(1,5000)*1000
        weight = round(random.uniform(0.1,10.0),1)

        product = {
            'product_name' : name,
            'product_category' : category,
            'product_price' : price, #rupiah
            'product_weight' : weight, # kilogram
        }

        products.append(product)

    return products