from main import (search, 
                  list_user_products, 
                  list_products_per_tag, 
                  add_product_to_catalog,
                  update_stock,
                  purchase_product,
                  remove_product)
from models import (Product, ProductTag, Tag, Transactions)
import pytest 


def test_search():
    array_term_silver = ['Silver Moon studs', 'Silver flower bangle', 'Lapis lazuli ring']
    array_term_flower = ['Sunflower studs', 'Silver flower bangle']
    none_existing_term = "sweater"
    assert type(search("silver")) == list
    assert search("silver") == array_term_silver
    assert search("Silver") == array_term_silver
    assert search("silve") == array_term_silver
    assert search("flower") == array_term_flower
    assert search("Flower") == array_term_flower
    assert search("flow") == array_term_flower
    assert search(none_existing_term) == []

# def test_list_user_products():
#     abels_products =["Lapis lazuli ring"]
#     jenny_products =["Silver Moon studs","Moonstone charm necklace"]
#     assert type(list_user_products(3)) == list
#     assert list_user_products(3) == abels_products
#     assert list_user_products(4) == jenny_products

def test_list_products_per_tag():
    products_tag_earrings = ['Sunflower studs', 'Silver Moon studs']
    products_tag_emerald= ['Beaded necklace']
    assert type(list_products_per_tag(4)) == list
    assert list_products_per_tag(4) == products_tag_earrings
    assert list_products_per_tag(11) == products_tag_emerald
    assert type(list_products_per_tag(13)) == list

def test_add_product_to_catalog():
    product =["Diamond Ring", 
              "pretty shiny ring", 
              150.50, 
              10,
              ["Diamond", "ring"]]
    add_product_to_catalog(1,product) 
    product_in_database = Product.get(Product.name == "Diamond Ring")
    assert product_in_database.name == "Diamond Ring"
    assert product_in_database.price_per_unit == 150.50
    assert product_in_database.owner_id == 1
    assert product_in_database.quantity_in_stock == 10
    assert product_in_database.description == "pretty shiny ring"
    diamond_tag = Tag.get(Tag.name =="diamond") 
    assert diamond_tag.id == 13

def test_update_stock():
     new_quantity = 50
     product_id = 1
     update_stock(product_id, new_quantity)
     product = Product.get(Product.id == 1)
     assert product.quantity_in_stock == new_quantity

def test_purchase_product():
    product_id = 2
    buyer_id = 2
    quantity = 1
    purchase_product(product_id, buyer_id, quantity)
    transaction = Transactions.select().join(Product).where(Transactions.id == 4)
    for purchase in transaction:
        assert purchase.product.id == 2
        assert purchase.buyer_id == 2
        assert purchase.quantity_bought == 1
        assert purchase.product.quantity_in_stock == 15

def test_remove_product():
    product_id = 3
    remove_product(3)
    with pytest.raises(Product.DoesNotExist):
       Product.get(Product.id == product_id)

       



  

