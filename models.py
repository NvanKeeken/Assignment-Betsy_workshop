# Models go here 
from peewee import (Model, 
                    SqliteDatabase, 
                    CharField, 
                    ForeignKeyField, 
                    IntegerField, 
                    DecimalField,
                    TextField,
                    BooleanField)
from peewee import Check
db = SqliteDatabase("betsy.db")

class BaseModel(Model):

    class Meta:
        database = db

class User(BaseModel):
  username = CharField(unique= True)
  email = CharField(unique=True)
  first_name = CharField()
  last_name = CharField()
  street_name = CharField()
  house_number = CharField() # charfield because house number can have a addition of a letter
  postal_code = CharField(max_length=10) # max length is 10 for postal code in the world 
  city = CharField()
  country = CharField(max_length=60) # longest country name has 56 charaters 
  billing_method = CharField()
  bank_account_number = CharField(unique = True)


class Product(BaseModel):
   name = CharField(index=True)
   description = TextField()
   price_per_unit = DecimalField(constraints=[Check("price_per_unit > 0")], decimal_places=2, max_digits=6, auto_round=True) 
   quantity_in_stock = IntegerField()
   owner = ForeignKeyField(User, backref="owned_products")

class Tag(BaseModel):
   name = CharField(unique= True)

class ProductTag(BaseModel):
   tag = ForeignKeyField(Tag, backref= "products")
   product = ForeignKeyField(Product, backref="tags")

class Transactions(BaseModel):
   product = ForeignKeyField(Product, backref="sales")
   buyer = ForeignKeyField(User, backref="purchases")
   quantity_bought = IntegerField()



