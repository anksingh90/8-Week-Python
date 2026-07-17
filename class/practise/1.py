'''Q4 : Task 4 — Hospital Patient System
Create a Person class with name and __age (private) with an age setter that rejects values below 0 or above 120.
Create a Patient class inheriting from Person, adding ailment and __admitted (private, default True)
Write a discharge() method that sets __admitted to False
Write save() that inserts the patient and stores the row ID
Write update_status() that runs an UPDATE query using the stored row ID to sync discharge status to the DB
Admit 2 patients, discharge one, sync to DB, then print all records showing current status'''

import sqlite3

con = sqlite3.connect("hospital.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS patients(
id INTEGER PRIMARY KEY,
name CHAR,
age CHAR,
ailment CHAR,
admitted CHAR
)
""")

class Person:                     # main()
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age

class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self.ailment = ailment
        self.__admitted = True

    def discharge(self):
        self.__admitted = False
        print(f"Discharging patient : {self.name} !")

    def save(self):
        cur.execute(
            "INSERT INTO patients(name,age,ailment,admitted) VALUES(?,?,?,?)",
            (self.name, self.get_age(), self.ailment, self.__admitted)
        )
        self.id = cur.lastrowid
        con.commit()
        print(f"Saving details of patient : {self.name}")

    def update_status(self):
        cur.execute(
            "UPDATE patients SET admitted=? WHERE id=?",
            (self.__admitted, self.id)
        )
        print(f"Updated details of patient : ID : {self.id}, Name : {self.name}")
        con.commit()

p1 = Patient("Prachi",17, "Fever")
p2 = Patient("Reeva",22, "Cold")
p1.save()
p2.save()

p1.discharge()
p1.update_status()

cur.execute("SELECT * FROM patients")
rows = cur.fetchall()

# printing details of all the patients !
print('**** Patient Details ****')
for i in rows:
        print(f"ID : {i[0]}, Name : {i[1]}, Age : {i[2]}, Symptoms : {i[3]}, Admitted : {i[4]}")

con.commit()
con.close()