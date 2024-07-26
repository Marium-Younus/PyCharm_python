class Brands: #parent,super,base
    brand_name1 ="Amazon"
    brand_name2 = "Ebay"
    brand_name3 = "OLX"

class Products(Brands): #child,sub,derived
    pro_1 ="Online Ecommerce Store"
    pro_2 = "Online Store"
    pro_3 = "Online Seller and buyer Store"

obj =Products()
print(obj.brand_name1," is an",obj.pro_1)
print(obj.brand_name2," is an",obj.pro_2)
print(obj.brand_name3," is an",obj.pro_3)