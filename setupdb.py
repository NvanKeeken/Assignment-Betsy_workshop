from models import (db, User, Product, Transactions, Tag, ProductTag)
import os

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy.db")
    if os.path.exists(database_path):
        os.remove(database_path)

def set_test_data():
    db.connect()

    db.create_tables([
        User,
        Product,
        Tag,
        Transactions,
        ProductTag
    ])

    # define test data per table
    users = [
              ["Louise", "Hendriks", "Bekerbaan", 
              "4", "6333 EZ", "Schimmert", 
              "The Netherlands", "457868"],

              ["Denis", "Jansen", "Hanewei", 
               "8a", "6344 GH", "Schinnen",
               "The Netherlands", "567897"],

               ["Abel", "Oliver", "Baker Street", 
                "11", "NW1", "London", 
                "UK", "678967"],

                ["Jenny", "Patterson", "Cannon Street", 
                 "12", "B2 5EP", "Birmingham", 
                 "UK", "56789"],

                 ["Helena", "Joosten", "Hoofdstraat", 
                  "62", "7311 At", "Apeldoorn", 
                  "The Netherlands", "467390"]
               ]

    products = []

    tags = []

    transactions = []

    product_tags = []

    # Insert new data per table
    for user in users:
        firstname, lastname, street, street_nr, postal_code, city, country, account_nr = user
        User.create(first_name = firstname, 
                    last_name = lastname,
                    street_name = street,
                    house_number = street_nr,
                    postal_code = postal_code,
                    city = city,
                    country = country,
                    bank_account_number = account_nr)