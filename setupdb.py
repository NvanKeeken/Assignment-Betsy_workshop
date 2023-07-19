from models import (db, User, Product, Transactions, Tag, ProductTag)
import os

def main():
    """
    Comment out the fuction you are not using and run the file.
    """
    populate_test_database()
    #delete_database()

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
    ])

    # Test-data per table 
    users = [
              {
                "username":"PrettyStones",
                "email":"prettystones@gmail.com",
                "first_name":"Louise", 
                "last_name":"Hendriks", 
                "street_name":"Bekerbaan",
                "house_number": "4", 
                "postal_code":"6333 EZ", 
                "city":"Schimmert", 
                "country":"The Netherlands",
                "billing_method":"IDEAL",
                "bank_account_number":"457868"},

              {
                  "username":"RusticMetals",
                  "email":"d.jansen@hotmail.com",
                  "first_name":"Denis", 
                  "last_name":"Jansen", 
                  "street_name":"Hanewei", 
                  "house_number":"8a", 
                  "postal_code":"6344 GH", 
                  "city":"Schinnen",
                  "country":"The Netherlands",
                  "billing_method":"Paypal",
                  "bank_account_number":"567897"}
               ,

               {
                "username":"Abel-Crystals",
                "email":"abel.oliver@gmail.com",
                "first_name":"Abel", 
                "last_name":"Oliver", 
                "street_name":"Baker Street", 
                "house_number":"11", 
                "postal_code":"NW1", 
                "city":"London", 
                "country":"UK",
                "billing_method":"Creditcard",
                "bank_account_number":"678967"},

                {
                 "username":"Jenny-Jewels",
                 "email":"jenny333@live.nl",
                 "first_name":"Jenny", 
                 "last_name":"Patterson", 
                 "street_name":"Cannon Street", 
                 "house_number":"12", 
                 "postal_code":"B2 5EP", 
                 "city":"Birmingham", 
                 "country":"UK",
                 "billing_method":"Creditcard",
                 "bank_account_number":"56789"},

                 {
                  "username":"Sunny-Jewelry",
                  "email":"sunnyjewelry@gmail.com",
                  "first_name":"Helena", 
                  "last_name":"Joosten", 
                  "street_name":"Hoofdstraat", 
                  "house_number":"62", 
                  "postal_code":"7311 At", 
                  "city":"Apeldoorn", 
                  "country":"The Netherlands",
                  "billing_method":"IDEAL", 
                  "bank_account_number":"467390"
               }]
   
    products = [
        {
            "name":"Sunflower studs", 
            "description":"handmade plastic earring studs for summer and spring",
            "price_per_unit":5.00,
            "quantity_in_stock": 3,
            "owner":5},
         
         {
            "name":"Silver Moon studs", 
            "description":"handmade moon earring silver studs with a stirling silver back",
            "price_per_unit":13.00, 
            "quantity_in_stock":16,
            "owner":4},
         
         {
            "name":"Moonstone charm necklace", 
            "description":"handmade golden chain necklace with a white moonstone charm",
            "price_per_unit":63.50, 
            "quantity_in_stock":6,
            "owner":4},
         
         {
            "name":"Beaded necklace", 
            "description":"handmade beaded necklace with round emerald beads",
            "price_per_unit":90.25, 
            "quantity_in_stock":20,
            "owner":1},
          
          {
           "name":"Personalised cuff bracelet", 
           "description":"handmade 14k golden cuff bracelet with a personalised message engraved on it",
           "price_per_unit":55.75, 
           "quantity_in_stock":15,
           "owner":2},

           {
            "name":"Silver flower bangle", 
            "description":"handmade silver bangle bracelet with daisies engraved on it",
            "price_per_unit":51.75, 
            "quantity_in_stock":15,
            "owner":5},

            {
             "name":"Rustic golden ring", 
             "description":"handmade 14k golden hammered ring", 
             "price_per_unit":38.00, 
             "quantity_in_stock":5,
             "owner":2},

             {
              "name":"Lapis lazuli ring", 
              "description":"handmade sirling silver ring with 4 mm gemstone", 
              "price_per_unit":22.75, 
              "quantity_in_stock":10,
               "owner":3}
    ]
    
    tags = [{"name":"ring"}, 
            {"name":"bracelet"}, 
            {"name":"necklace"}, 
            {"name":"earrings"},
            {"name":"gold"}, 
            {"name":"silver"}, 
            {"name":"rosegold"}, 
            {"name":"plastic"},
            {"name":"tiger eye"}, 
            {"name":"moonstone"}, 
            {"name":"emerald"}, 
            {"name":"lapis lazuli"}]

    transactions = [
        [4, 5, 3],
        [2, 1, 1],
        [5, 3, 2]
    ]
    
    product_tags = [(1, [4, 8]), 
                    (2, [4, 6]),
                    (3, [3, 5, 10]),
                    (4, [3, 5, 11]),
                    (5, [2, 5]), 
                    (6, [1, 6]),
                    (7, [1, 5]), 
                    (8, [1, 12])]

    # Insert new data per table
   
    with db.atomic():
        # bulk inserts
        User.insert_many(users).execute()
        Product.insert_many(products).execute()
        Tag.insert_many(tags).execute()
        Transactions.insert_many(transactions).execute() 

        # Insert ProductTag
        for product, tag_names in product_tags:
           for tag_name in tag_names:
               ProductTag.create(tag= tag_name, product= product)


if __name__ == "__main__":
    main()