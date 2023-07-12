# Models go here 
from peewee import (Model, 
                    SqliteDatabase, 
                    CharField, 
                    ForeignKeyField, 
                    IntegerField, 
                    DecimalField,
                    TextField)

db = SqliteDatabase("betsy.db")

class BaseModel(Model):

    class Meta:
        database = db

class User(BaseModel):
  first_name = CharField()
  last_name = CharField()
  street_name = CharField()
  house_number = CharField() # charfield because house number can have a addition of a letter
  postal_code = CharField(max_length=10) # max amount of digits is 10 for postal code in the world 
  city = CharField()
  country = CharField(max_length=60) # longest country name has 56 charaters 
  bank_account_number = CharField(unique = True)

class Product(BaseModel):
   name = CharField()
   description = TextField()
   price_per_unit = DecimalField(decimal_places=2) # or floatfield
   quantity_in_stock = IntegerField()

class Tag(BaseModel):
   name = CharField(unique= True)

class ProductTag(BaseModel):
   tag = ForeignKeyField(Tag, backref= "products")
   product = ForeignKeyField(Product, backref="tags")

class Transactions(BaseModel):
   product = ForeignKeyField(Product, backref="sales")
   buyer = ForeignKeyField(User, backref="purchases")
   quantity_bought = IntegerField()



