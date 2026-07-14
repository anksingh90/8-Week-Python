'''
Write a Python script : 
a. create a class that accepts - make, model, date_of_purchase
b. setup database connection to db - carsdb and store info into table - cars
c. Store object details in db
'''

import sqlite3
from datetime import datetime

class Car:
    def __init__(self, make, model, date_of_purchase):
        self.make = make
        self.model = model
        self.date_of_purchase = date_of_purchase

# 1. Connect to the database (it creates 'cars.db' for you)
conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

# 2. Create a table to store the car data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        make TEXT,
        model TEXT,
        date_of_purchase DATE
    )
''')

# 3. Create a Car object

m_name = input('Enter car Manufacture name : ')
c_name = input('Enter car Model name : ')

current_datetime = datetime.now()
p_date = current_datetime.strftime("%Y-%m-%d")

my_car = Car(m_name, c_name, p_date)

# 4. Insert the car data into the database
cursor.execute('''
    INSERT INTO cars (make, model, date_of_purchase)
    VALUES (?, ?, ?)
''', (my_car.make, my_car.model, my_car.date_of_purchase))

# 5. Save the changes and close the connection
conn.commit()
conn.close()