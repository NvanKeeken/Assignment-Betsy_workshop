## Models
you make a site where you can sell homemade goods. 

user must have:
- name 
- adress data
- billing information

     class User(model):
        name = CharField()
        adress_data = CharField()
        billing_info = CharField()
        products_owned = ManyToManyField() or number 

product must have:
- name
- description
- price per unit
- quantity describing amount in stock
priced stored in safe way rouding numbers should be impossible / afronden 2 dec

    class Product(model):
        name = CharField()
        description = CharField()
        price_per_unit = FloatField()
        amount_in_stock = IntegerField()

track purchases in transaction model made on the marketplace, only users can purchase goods
it must link a buyer with a purchased product and quentity of purchased items 
transaction enkelvoud kan niet gereserveerd woord
    class Transactions(model):
        purchased_product = ForeignKeyField(Product)
        buyer = ForeignKeyField(User)
        amount_of_purchased_products = IntegerField()
    
the tags should not be duplicated 
    class Tag(model):
        name = CharField()

    class product_tag(model):
        tag_id = Foreignkeyfield()
        product_id = Foreignkeyfield()

User:
-first_name
-last_name
-streetname
-house_number
-postal_code
-city
-country 
- bank_account_number

Product:
-name 
-description 
-price_per_unit
-quantity_in_stock

Transaction:
-product 
-buyer 
-quantity_bought

Tag:
- name

ProductTag:
- product (id)
- tag (id)

OwnedProduct :
- product (id)
- user (id)
## Constraints 
Constraints are restrictions imposed on the possible values that can be put in a field. One such constraint is primary key.

- The tags should not be duplicated
    unique = True
  If a field is not a primary key, still it can be constrained to store unique values in table.
- Possibly a house number addition constraint null allows null values
      null = True
- The price should be stored in a safe way; rounding errors should be impossible.
  if you use DecimalField special parameters to use are decimal_places 
    decimal_places = 2
- on charfield you can add a constraint max_digits to limit the amount of characters 
  for example for postal code or bank account. 
     - PostalCode: The country with the most amount of digits for postal code is 10  
          so max_digits = 10 or 12 if you want to include future changes
     - IBAN: contains up to 34 alphanumeric characters 
          so max_digits = 34 and it has to be unique=True
     - Price_per_unit: is not 0 
         class Meta:
             constraints=[Check('price_per_unit>0')]

## TEST DATA
possible users:
- PrettyStones, Louise, Hendriks, bekerbaan, 4,6333 EZ, Schimmert, The Netherlands, 457868 
- RusticMetals, Denis, Jansen, hanenwei, 8, 6344 GH, Schinnen, The Netherlands, 567897
- Abels-Crystals, Abel, Oliver, Baker street, 11, NW1, London, UK, 678967,
- Jenny-Jewels,Jenny, Patterson, Cannon street, 12, B2 5EP, Birmingham, Uk, 56789
- Sunny-Jewelry, Helena, Joosten, Hoofdstraat, 62, 7311 AT, Apeldoorn, The Netherlands, 467390

email:
prettystones@gmail.com
d.jansen@hotmail.com
abel.oliver@gmail.com
jenny333@live.nl
sunnyjewelry@gmail.com


possible products:
- Sunflower studs, handmade plastic earing studs cute for summer and spring, 5.00, 3
- Silver Moon studs, handmade Moon earing studs from silver with stirling silver backs, 13.00, 16
- Moonstone Charm necklace, handmade golden chain necklace with a white moonstone charm, 63.50, 6
- Beaded necklace, handmade beaded necklace with round emerald beads, 89.00, 20
- Personalised cuff bracelet, handmade golden cuff bracelet with personalised message engraved, 51.75, 20
- Silver flower bangle, handmade silver bangle bracelet with daisies engraved on it, 55.75, 15
- Hammered golden ring, handmade 14k gold with a rustic look, 38.00, 5
- lapis lazuli ring, handmade stirling silver ring with 4 mm gemstone, 22.75, 10  

possible tags:
- jewellry 
   -ring      -gold
   -bracelet   -silver   - emerald         
   -necklace   -rosegold -lapis lazuli
   -earrings   -plastic  -tiger eye

- clothing 
  -pants 
  -sweatshirt 
  -t-shirt 
  -dress 

- furniture 
  -chair
  -table
  -

Possible productTag:
- 1, earrings, plastic
- 2, earings, silver
- 3, necklace, gold, moonstone
-4, necklace, emerald 
-5,bracelet, gold 
-6, bracelet, silver
-7, ring, gold
-7, ring, lapis lazuli

possible transactions:
- product buyer, quantity_bought
- Silver Moon studs, Louise, Hendriks, 1
-Personalised cuff bracelet, Abel, Oliver, 2
- Beaded necklace, Helena, Joosten, 3 

possible ownend products:
- Jenny, Patterson, Silver Moon studs, Moonstone Charm necklace 
-Denis, Jansen, Hammerd golden ring, Personalised cuff bracelet 
- Abel, Oliver, Lapis lazuli ring
-Louise, Hendriks, Beaded necklace 
-Helena, Joosten, Sunflower studs, Silver flower bangle  
        
nog moeten doen:
- try catch
- billing method choices
- bulk insert

