# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line

from models import (User, Product, Transactions, Tag, ProductTag, db)

def search(term):
    ...


def list_user_products(user_id):
    ...


def list_products_per_tag(tag_id):
    products_per_tag = []
    products = ProductTag.select().where(ProductTag.tag == tag_id)
    for product in products:
       products_per_tag.append(product.product)
    return products_per_tag


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    product = Product.get(Product.id == product_id)
    product.quantity_in_stock = new_quantity
    product.save()


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...
