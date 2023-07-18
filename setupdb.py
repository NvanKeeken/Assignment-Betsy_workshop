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
            "description":"handmade plastic earing studs for summer and spring",
            "price_per_unit":5.00,
            "quantity_in_stock": 3,
            "owner":"Sunny-Jewelry"},
         
         {
            "name":"Silver Moon studs", 
            "description":"handmade moon earing silver studs with a stirling silver back",
            "price_per_unit":13.00, 
            "quantity_in_stock":16,
            "owner":"Jenny-Jewels"},
         
         {
            "name":"Moonstone charm necklace", 
            "description":"handmade golden chain necklace with a white moonstone charm",
            "price_per_unit":63.50, 
            "quantity_in_stock":6,
            "owner":"Jenny-Jewels"},
         
         {
            "name":"Beaded necklace", 
            "description":"handmade beaded necklace with round emerald beads",
            "price_per_unit":90.25, 
            "quantity_in_stock":20,
            "owner":"PrettyStones"},
          
          {
           "name":"Personalised cuff bracelet", 
           "description":"handmade 14k golden cuff bracelet with a personalised message engraved on it",
           "price_per_unit":55.75, 
           "quantity_in_stock":15,
           "owner":"RusticMetals"},

           {
            "name":"Silver flower bangle", 
            "description":"handmade silver bangle bracelet with daisies engraved on it",
            "price_per_unit":51.75, 
            "quantity_in_stock":15,
            "owner":"Sunny-Jewelry"},

            {
             "name":"Rustic golden ring", 
             "description":"handmade 14k golden hammered ring", 
             "price_per_unit":38.00, 
             "quantity_in_stock":5,
             "owner":"RusticMetals"},

             {
              "name":"Lapis lazuli ring", 
              "description":"handmade sirling silver ring with 4 mm gemstone", 
              "price_per_unit":22.75, 
              "quantity_in_stock":10,
               "owner":"Abel-Crystals"}
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
        ["Beaded necklace", "Helena", "Joosten", 3],
        ["Silver Moon studs", "Louise", "Hendriks", 1],
        ["Personalised cuff bracelet", "Abel", "Oliver", 2]
    ]
    
    product_tags = [("Sunflower studs", ["earrings", "plastic"]), 
                    ("Silver Moon studs", ["earrings", "silver"]),
                    ("Moonstone charm necklace", ["necklace", "gold","moonstone"]),
                    ("Beaded necklace", ["necklace","gold", "emerald"]),
                    ("Personalised cuff bracelet", ["bracelet", "gold"]), 
                    ("Silver flower bangle", ["ring", "silver"]),
                    ("Rustic golden ring", ["ring", "gold"]), 
                    ("Lapis lazuli ring", ["ring", "lapis lazuli"])]

    # Insert new data per table
   
    with db.atomic():
        # bulk inserts
        User.insert_many(users).execute()
        Product.insert_many(products).execute()
        Tag.insert_many(tags).execute()
        
        # Insert Transactions
        for product, firstname, lastname, quantity in transactions:
           buyer = User.get(User.first_name == firstname and User.last_name == lastname)
           product_id = Product.get(Product.name == product)
           Transactions.create(
               product = product_id, 
               buyer = buyer, 
               quantity_bought = quantity)
           
        # Insert ProductTag
        for product, tag_names in product_tags:
           product = Product.get(Product.name == product)
           for tag_name in tag_names:
               tag = Tag.get(Tag.name == tag_name)
               ProductTag.create(tag= tag, product= product)
        
populate_test_database()