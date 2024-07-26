
class Brands:
    brand_name1 ="Amazon"
    brand_name2 = "Ebay"
    brand_name3 = "OLX"

class Products(Brands):
    prod_1 ="Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"

obj_1 = Products()

print(obj_1.brand_name1 + " is an "+obj_1.prod_1)
print(obj_1.brand_name2 + " is an "+obj_1.prod_2)
print(obj_1.brand_name3 + " is an "+obj_1.prod_3)

