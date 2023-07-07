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
    users = []

    products = []

    tags = []

    transactions = []

    product_tags = []

    # Insert new data per table