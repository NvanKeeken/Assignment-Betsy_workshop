# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line
from models import (User, Product, Transactions, Tag, ProductTag,db)
from peewee import JOIN

def search(term):
    product_contain_term =[]
    products_contain_search = Product.select().where(Product.name.contains(term) | Product.description.contains(term))
    for product in products_contain_search:
        product_contain_term.append(product.name)
    return product_contain_term


def list_user_products(user_id):
    products_of_user = []
    products_owned_by_user= (
        Product.select()
        .join(User)
        .where(Product.owner == user_id)
    )
    # products_owned_by_user = OwnedProduct.select().where(OwnedProduct.seller == user_id)
    for product in products_owned_by_user:
         products_of_user.append(product.name)
    return products_of_user

def list_products_per_tag(tag_id):
    products_per_tag = []
    products = (
        ProductTag.select()
        .join(Product)
        .where(ProductTag.tag == tag_id)
    )
    # products = ProductTag.select().where(ProductTag.tag == tag_id)
    for product in products:
        products_per_tag.append(product.product.name)
    return products_per_tag


def add_product_to_catalog(user_id, product):
    name,description, price, quantity= product
    new_product,_ = Product.get_or_create(
        name= name,
        defaults= {
            "description": description,
            "price_per_unit": price,
            "quantity_in_stock": quantity,
            "owner": user_id
            }
    )
    return new_product.name
    # OwnedProduct.create(seller= user_id, product= new_product)
# add_product_to_catalog(1,["Diamond ring", "handmade diamond ring", 
#               34.00, 5,])   

def update_stock(product_id, new_quantity):
    product = Product.get(Product.id == product_id)
    product.quantity_in_stock = new_quantity
    product.save()

"""To handle a purchase there are two main things that need to happen, 
a new transaction needs to be added to a buyer in Transactions model
and the stock of the product needs to be updatet """

def purchase_product(product_id, buyer_id, quantity):
    # Adds a new transaction to buyer 
    Transactions.create(product= product_id, 
                         buyer= buyer_id,
                         quantity_bought= quantity)
    # Updates stock of the product 
    product_quantity = Product.get(Product.id == product_id).quantity_in_stock
    new_quantity_in_stock = product_quantity - quantity
    if new_quantity_in_stock >= 0:
       update_stock(product_id, new_quantity_in_stock)


def remove_product(product_id):
    product_removed = Product.get(Product.id == product_id)
    product_removed.delete_instance()