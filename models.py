# Models go here 

from peewee import Check
from peewee import (Model, 
                    SqliteDatabase, 
                    CharField, 
                    ForeignKeyField, 
                    IntegerField, 
                    DecimalField,
                    TextField)
# Modelling

db = SqliteDatabase("betsy.db")

class BaseModel(Model):

    class Meta:
        database = db


# User Model conditions: A user has a name, address data, and billing information.
class User(BaseModel):
  username = CharField(unique= True, max_length=50)
  email = CharField(unique=True)
  # name
  first_name = CharField()
  last_name = CharField()
  # address data
  street_name = CharField()
  house_number = CharField() 
  postal_code = CharField(max_length=10) 
  city = CharField()
  country = CharField() 
  #billing information
  billing_method = CharField()
  bank_account_number = CharField(unique = True)

"""Product model conditions:The products must have a name, 
a description, a price per unit, and a quantity describing the amount in stock."""
class Product(BaseModel):
   name = CharField(index=True) # products are indexed 
   description = TextField()
   # decimal_places and auto_round are used to store price in save way
   price_per_unit = DecimalField(constraints=[Check("price_per_unit > 0")], 
                                 decimal_places=2, 
                                 max_digits=6, 
                                 auto_round=True)  
   quantity_in_stock = IntegerField()
   owner = ForeignKeyField(User, backref="owned_products") 

# Tag model conditions: The tags should not be duplicated so unique constraint is used
class Tag(BaseModel):
   name = CharField(unique= True)

"""ProductTag model contains the relation between the product and tags
A product can have multiple tags"""
class ProductTag(BaseModel):
   tag = ForeignKeyField(Tag, backref= "products")
   product = ForeignKeyField(Product, backref="tags")

"""Transaction model conditions: must link a buyer with a purchased product and a quantity of purchased items """
class Transactions(BaseModel):
   product = ForeignKeyField(Product, backref="sales")
   buyer = ForeignKeyField(User, backref="purchases")
   quantity_bought = IntegerField()



