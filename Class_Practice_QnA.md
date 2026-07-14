**Question 1: The E-Commerce Inventory System (Table-per-Hierarchy Strategy)**  
**Objective:** Design a product inventory system using inheritance where a parent class and its child classes share a single database table, utilizing a "discriminator" column to identify the product type.  
**Scenario:** An online store sells two types of products: Physical Books and Digital Software. All products have a title and a price. Books require a weight attribute (for shipping fees), while Software requires a file size attribute (for download allocation).  

---

**Task Requirements:**
1. **OOP Design :**  
   - Create a base class `Product` with `title` and `price`.
   - Create a child class `Book` that inherits from `Product` and adds a `weight` attribute.
   - Create a child class `Software` that inherits from `Product` and adds a `file_size` attribute.

2. **Database Setup :**  
   - Connect to an SQLite database named `inventory.db`
   - Create a single table named products. The schema must include an `id`,
       - `product_type` (TEXT, to act as a discriminator: 'Book' or 'Software'),
       - `title`, `price`, `weight` (NULLable), and `file_size` (NULLable).

3. **Task :**  
  - Write an instance method inside the base or child classes called `save_to_db(self, conn)`
  - When a Book object calls this method, it should insert `'Book'` into the `product_type` column and leave `file_size` as `None`.
  - When a `Software` object calls it, it should insert `'Software'` into `product_type` and leave `weight` as `None`.

4. **Retrieval Function :**  
  - Write a separate function `get_all_products(conn)` that queries the database, reads the records, dynamically instantiates the correct Python object (Book or Software) based on the product_type column, and returns a list of these objects.

---  

**Question 2: Corporate Payroll & Foreign Key Relationships (Table-per-Class Strategy)**  
**Objective:** Implement class inheritance that maps directly to a normalized, multi-table database schema using foreign key constraints to link parent and child data.  
**Scenario:** A company tracks its staff using an inheritance structure. All workers are `Employees`, but some are specialized `Managers`.  

**Task Requirements:**
1. **OOP Design :**  
   - Create a base class `Employee` with attributes: `emp_id` (string), `name`, and `base_salary`.
   - Create a child class `Manager` that inherits from `Employee` and adds a `bonus` attribute.
   
2. **Database Setup :**  
   - Connect to an SQLite database named `company.db` and enable foreign key support (`PRAGMA foreign_keys = ON;`)
   - Create an `employees` table: `emp_id` (PRIMARY KEY), `name`, and `base_salary`
   - Create a separate `managers` table: `emp_id` (PRIMARY KEY, FOREIGN KEY referencing employees(emp_id) on delete cascade) and `bonus`.

3. **Task :**  
  - Implement a `save(self, cursor)` method in the `Employee` class that inserts data only into the `employees` table.
  - Override the `save(self, cursor)` method in the `Manager` class. It must call `super().save(cursor)` first to populate the parent table, and then explicitly insert the manager-specific `bonus` into the `managers` table within the same database transaction.

4. **Validation Test :**  
  - Instantiate one regular employee object and one manager object. Save both to the database, commit the transaction, and handle any potential integrity errors cleanly if a duplicate `emp_id` is entered.

---  

** End of File **
