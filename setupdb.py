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

    products = [
        ["Sunflower studs", "handmade plastic earing studs for summer and spring",
         5.00, 3],
         
         ["Silver Moon studs", "handmade moon earing silver studs with a stirling silver back",
         13.00, 16],
         
         ["Moonstone charm necklace", "handmade golden chain necklace with a white moonstone charm",
         63.50, 6],
         
         ["Beaded necklace", "handmade beaded necklace with round emerald beads",
          90.25, 20],
          
          ["Personalised cuff bracelet", "handmade 14k golden cuff bracelet with a personalised message engraved on it",
           55.75, 15],

           ["Silver flower bangle", "handmade silver bangle bracelet with daisies engraved on it",
            51.75, 15],

            ["Rustic golden ring", "handmade 14k golden hammered ring", 
             38.00, 5],

             ["Lapis lazuli ring", "handmade sirling silver ring with 4 mm gemstone", 
              22.75, 10]
    ]

    tags = ["ring", "bracelet", "necklace", "earrings",
            "gold", "silver", "rosegold", "plastic",
            "tiger eye", "moonstone", "emerald", "lapis lazuli"]

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
        
    for product in products:
        name, description, price, stock = product
        Product.create(name = name,
                       description = description,
                       price_per_unit = price,
                       quantity_in_stock = stock)
    for tag in tags:
         Tag.create(name = tag)