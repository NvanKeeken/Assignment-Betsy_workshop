# Models go here 
from peewee import (Model, 
                    SqliteDatabase, 
                    CharField, 
                    ForeignKeyField, 
                    IntegerField, 
                    FloatField)

db = SqliteDatabase("betsy.db")

class BaseModel(Model):

    class Meta:
        database = db

class User(BaseModel):
  first_name = CharField()
  last_name = CharField()
  street_name = CharField()
  house_number = CharField() # charfield because house number can have a addition of a letter
  postal_code = CharField() 
  city = CharField()
  country = CharField()
  bank_account_number = CharField()

class Product(BaseModel):
   pass

class Tag():
   pass

class ProductTag():
   pass

class Transactions():
   pass