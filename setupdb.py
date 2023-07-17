from models import (db, User, Product, Transactions, Tag, ProductTag)
import os

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy.db")
    if os.path.exists(database_path):
        os.remove(database_path)

def populate_test_database():
    db.connect()

    db.create_tables([
        User,
        Product,
        Tag,
        Transactions,
        ProductTag,
        # OwnedProduct
    ])

    # define test data per table
    users = [
              ["PrettyStones","Louise", "Hendriks", "Bekerbaan", 
              "4", "6333 EZ", "Schimmert", 
              "The Netherlands", "457868"],

              ["RusticMetals","Denis", "Jansen", "Hanewei", 
               "8a", "6344 GH", "Schinnen",
               "The Netherlands", "567897"],

               ["Abel-Crystals","Abel", "Oliver", "Baker Street", 
                "11", "NW1", "London", 
                "UK", "678967"],

                ["Jenny-Jewels","Jenny", "Patterson", "Cannon Street", 
                 "12", "B2 5EP", "Birmingham", 
                 "UK", "56789"],

                 ["Sunny-Jewelry","Helena", "Joosten", "Hoofdstraat", 
                  "62", "7311 At", "Apeldoorn", 
                  "The Netherlands", "467390"]
               ]

    # products = [
    #     ["Sunflower studs", "handmade plastic earing studs for summer and spring",
    #      5.00, 3],
         
    #      ["Silver Moon studs", "handmade moon earing silver studs with a stirling silver back",
    #      13.00, 16],
         
    #      ["Moonstone charm necklace", "handmade golden chain necklace with a white moonstone charm",
    #      63.50, 6],
         
    #      ["Beaded necklace", "handmade beaded necklace with round emerald beads",
    #       90.25, 20],
          
    #       ["Personalised cuff bracelet", "handmade 14k golden cuff bracelet with a personalised message engraved on it",
    #        55.75, 15],

    #        ["Silver flower bangle", "handmade silver bangle bracelet with daisies engraved on it",
    #         51.75, 15],

    #         ["Rustic golden ring", "handmade 14k golden hammered ring", 
    #          38.00, 5],

    #          ["Lapis lazuli ring", "handmade sirling silver ring with 4 mm gemstone", 
    #           22.75, 10]
    # ]
    products = [
        ["Sunflower studs", "handmade plastic earing studs for summer and spring",
         5.00, 3,"Sunny-Jewelry"],
         
         ["Silver Moon studs", "handmade moon earing silver studs with a stirling silver back",
         13.00, 16,"Jenny-Jewels"],
         
         ["Moonstone charm necklace", "handmade golden chain necklace with a white moonstone charm",
         63.50, 6,"Jenny-Jewels"],
         
         ["Beaded necklace", "handmade beaded necklace with round emerald beads",
          90.25, 20,"PrettyStones"],
          
          ["Personalised cuff bracelet", "handmade 14k golden cuff bracelet with a personalised message engraved on it",
           55.75, 15,"RusticMetals"],

           ["Silver flower bangle", "handmade silver bangle bracelet with daisies engraved on it",
            51.75, 15,"Sunny-Jewelry"],

            ["Rustic golden ring", "handmade 14k golden hammered ring", 
             38.00, 5,"RusticMetals"],

             ["Lapis lazuli ring", "handmade sirling silver ring with 4 mm gemstone", 
              22.75, 10,"Abel-Crystals"]
    ]
    tags = ["ring", "bracelet", "necklace", "earrings",
            "gold", "silver", "rosegold", "plastic",
            "tiger eye", "moonstone", "emerald", "lapis lazuli"]

    transactions = [
        ["Beaded necklace", "Helena", "Joosten", 3],
        ["Silver Moon studs", "Louise", "Hendriks", 1],
        ["Personalised cuff bracelet", "Abel", "Oliver", 2]
    ]
    
    owned_products = [
        ["Jenny", "Patterson",["Silver Moon studs", "Moonstone charm necklace"]],
        ["Dennis", "Jansen", ["Rustic golden ring", "Personalised cuff bracelet"]],
        ["Abel", "Oliver", ["Lapis lazuli ring"]],
        ["Louise", "Hendriks", ["Beaded necklace"]],
        ["Helena", "Joosten", ["Sunflower studs", "Silver flower bangle"]]

    ]
    product_tags = [(1, [4, 8]), (2, [4, 6]), (3, [3, 5, 10]),
                    (4, [3, 11]), (5, [2, 5]), (6, [2, 6]),
                    (7, [1, 5]), (8, [1, 12])]

    # Insert new data per table
    for user in users:
        username, firstname, lastname, street, street_nr, postal_code, city, country, account_nr = user
        User.create(username = username,
                    first_name = firstname, 
                    last_name = lastname,
                    street_name = street,
                    house_number = street_nr,
                    postal_code = postal_code,
                    city = city,
                    country = country,
                    bank_account_number = account_nr)
        
    for product in products:
        name, description, price, stock, owner = product
        product_owner = User.get(User.username == "Abel-Crystals")
        Product.create(name = name,
                       description = description,
                       price_per_unit = price,
                       quantity_in_stock = stock,
                       owner = product_owner)
    for tag in tags:
         Tag.create(name = tag)
    
    for product, firstname, lastname, quantity in transactions:
        buyer = User.get(User.first_name == firstname and User.last_name == lastname)
        product_id = Product.get(Product.name == product)
        Transactions.create(
            product = product_id, 
            buyer = buyer, 
            quantity_bought = quantity)
        
    # for firstname, lastname, user_products in owned_products:
    #     seller = User.get(User.first_name == firstname and User.last_name == lastname)
    #     for user_product in user_products:
    #         product = Product.get(Product.name == user_product)
    #         OwnedProduct.create(seller = seller, product= product) 

    for product, tag_names in product_tags:
        product = Product.get(Product.id == product)
        for tag_name in tag_names:
            tag = Tag.get(Tag.id == tag_name)
            ProductTag.create(tag= tag, product= product)
populate_test_database()