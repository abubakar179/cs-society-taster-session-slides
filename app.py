import sqlite3
from faker import Faker
import random

# Initialize Faker and database
fake = Faker()
conn = sqlite3.connect("/mnt/data/shop.db")
c = conn.cursor()

# Drop and recreate tables
c.execute('DROP TABLE IF EXISTS products')
c.execute('DROP TABLE IF EXISTS users')
c.execute('DROP TABLE IF EXISTS orders')

c.execute('CREATE TABLE products (id INTEGER, name TEXT, price INTEGER)')
c.execute('CREATE TABLE users (id INTEGER, username TEXT, password TEXT, email TEXT, address TEXT, card_number TEXT)')
c.execute('CREATE TABLE orders (id INTEGER, user_id INTEGER, product_id INTEGER)')

# Add products
products = [
    (1, 'Laptop', 999),
    (2, 'USB Stick', 10),
    (3, 'Rubber Duck', 2),
    (4, 'Gaming Mouse', 49),
    (5, 'Mechanical Keyboard', 129),
    (6, '27" Monitor', 299),
    (7, 'Webcam', 59),
    (8, 'External Hard Drive', 89),
    (9, 'Desk Lamp', 25),
    (10, 'Bluetooth Speaker', 35)
]
c.executemany('INSERT INTO products VALUES (?, ?, ?)', products)

# Generate fake users
users = []
for i in range(1, 101):
    username = fake.user_name()
    password = fake.password()
    email = fake.email()
    address = fake.address().replace('\n', ', ')
    card = fake.credit_card_number(card_type=None)
    users.append((i, username, password, email, address, card))

c.executemany('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', users)

# Generate fake orders
orders = []
for i in range(1, 151):
    user_id = random.randint(1, 100)
    product_id = random.randint(1, 10)
    orders.append((i, user_id, product_id))

c.executemany('INSERT INTO orders VALUES (?, ?, ?)', orders)

# Commit and close
conn.commit()
conn.close()
