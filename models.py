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
  pass

class Product(BaseModel):
   pass

class Tag():
   pass

class ProductTag():
   pass

class Transactions():
   pass