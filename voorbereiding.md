## Models
you make a site where you can sell homemade goods. 

user must have:
- name 
- adress data
- billing information

     class User(model):
        name = CharField()
        adress_data = CharField()
        billing_info = CharField()
        products_owned = ManyToManyField() or number 

product must have:
- name
- description
- price per unit
- quantity describing amount in stock
priced stored in safe way rouding numbers should be impossible / afronden 2 dec

    class Product(model):
        name = CharField()
        description = CharField()
        price_per_unit = FloatField()
        amount_in_stock = IntegerField()

track purchases in transaction model made on the marketplace, only users can purchase goods
it must link a buyer with a purchased product and quentity of purchased items 
transaction enkelvoud kan niet gereserveerd woord
    class Transactions(model):
        purchased_product = ForeignKeyField(Product)
        buyer = ForeignKeyField(User)
        amount_of_purchased_products = IntegerField()
    
the tags should not be duplicated 
    class Tag(model):
        name = CharField()

    class product_tag(model):
        tag_id = Foreignkeyfield()
        product_id = Foreignkeyfield()



User:
-first_name
-last_name
-streetname
-house_number
-postal_code
-city
-country 
- bank_account_number

Product:
-name 
-description 
-price_per_unit
-quantity_in_stock