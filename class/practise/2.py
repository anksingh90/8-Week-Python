'''Task 3 — Employee and Manager System
Create an Employee class with name, department, and __salary (private).

Add a salary property with a setter that rejects negative values
Create a Manager class that inherits from Employee and adds team_size
Both save into the same table staff in company.db with a role column storing "Employee" or "Manager"
Write an update_salary() method that updates the salary in the database for an existing record
Save 2 employees and 1 manager, update one employee's salary, then print all records from the DB'''



import sqlite3

conn = sqlite3.connect("company.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS staff(name VARCHAR, department VARCHAR, salary INT, team_size INT, role VARCHAR)")

class Employee:
    def __init__(self, name, depart, salary):
        self.name = name
        self.department = depart
        self.__salary = salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    def save(self):
        cur.execute("INSERT INTO staff VALUES(?,?,?,?,?)", (self.name, self.department, self.__salary, 0, "Employee"))
        conn.commit()

    def update_salary(self, salary):
        self.set_salary(salary)
        cur.execute("UPDATE staff SET salary=? WHERE name=?", (self.__salary, self.name))
        conn.commit()


class Manager(Employee):
    def __init__(self, name, department, salary, team_size):
        super().__init__(name, department, salary)
        self.team_size = team_size

    def save(self):
        cur.execute("INSERT INTO staff VALUES(?,?,?,?,?)", (self.name, self.department, self._Employee__salary, self.team_size, "Manager"))
        conn.commit()


e1 = Employee("Prachi", "IT", 30000)
e2 = Employee("Niket", "HR", 25000)
m1 = Manager("Reeva", "Sales", 50000, 5)

e1.save()
e2.save()
m1.save()

e1.update_salary(45000)

cur.execute("SELECT * FROM staff")
for i in cur.fetchall():
    print(i)
conn.commit()
conn.close()