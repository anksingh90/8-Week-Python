# Library Management System.py

import sqlite3
DB = "library.db"

# ---------------- BOOK CLASS ----------------
class Book:

    def __init__(self,isbn,title,author,genre,total,available):  
        # Enforcing types here prevents silent bugs later on. 
        # Casting isbn to a string fixes the INTEGER vs VARCHAR mismatch we noticed earlier!
        self.isbn = isbn        # recommendation - self.isbn = str(isbn)
        self.title = title
        self.author = author
        self.genre = genre
        self.total = total
        self.available = available

    def __str__(self):
        # User-facing output (triggered when you write: print(book))
        return f"{self.title} by {self.author} (Available: {self.available}/{self.total})"

    def __repr__(self):
        # Developer-facing output (helpful for debugging in the terminal)
        return (f"Book(isbn='{self.isbn}', "
                f"Title = '{self.title}', "
                f"Author = '{self.author}', "
                f"Genre = '{self.genre}', "
                f"Total = {self.total}, "
                f"Available = {self.available})")
 
    def __eq__(self, other):
        # Compare this(self) book against another(other) object using the unique ISBN
        return self.isbn == other.isbn

    # Adding new method
    # A clean way to check availability without exposing the raw logic everywhere 
    @property
    def is_available(self):
        return self.available > 0

# ---------------- MEMBER CLASS ----------------

class Member:

    def __init__(self, member_id, name, email, join_date, library=None):
        # Type casting ensures consistent data handling
        self.member_id = member_id
        self.name = name
        self.email = email
        self.join_date = join_date

        # Pass the library instance, so the member can query its own transactions
        self.library = library

    def __str__(self):
        # String representation for the user
        return f"Member: {self.name} (ID: {self.member_id})"

    # added new method !
    def __repr__(self):
        return (f"Member(member_id={self.member_id}, name='{self.name}', "
                f"email='{self.email}', join_date='{self.join_date}')")

    # Added new method
    # To check if two variables refer to the exact same member by comparing their unique member_id
    # Allows to compare two members: member1 == member2
    def __eq__(self, other):
        if isinstance(other, Member):
            return self.member_id == other.member_id
        return False

    @property
    def borrowed_count(self):
        if self.library is None:        # Dynamic property querying the database.
            return 0

        cur = self.library.conn.cursor()

        cur.execute("""
        SELECT COUNT(*)
        FROM transactions
        WHERE member_id=?
        AND return_date IS NULL
        """, (self.member_id,))

        return cur.fetchone()[0]


# ---------------- LIBRARY CLASS ----------------

class Library:

    def __init__(self, db=DB):
        # The constructor to establishes the initial state of the object.
        # It opens the connection to SQLite and triggers table creation immediately.
        self.conn = sqlite3.connect(db)
        self.books = []
        self.i = 0      # Manual counter
        self.create_tables()

    @classmethod
    def from_database(cls, db):     # Alternative constructor: creates a Library object from database data.
        return cls(db)

    # This method makes the Library "iterable", use it in a for-loop.
    def __iter__(self):
        self.load_books()       # Loads the data from the database and resets counter (self.i) to 0.
        self.i = 0
        return self

    def __next__(self):
        # This works hand-in-hand with __iter__. Every time the for-loop loops, 
        # it calls __next__ to get the next item, until it hits StopIteration.
        if self.i >= len(self.books):
            raise StopIteration
        
        book = self.books[self.i]
        self.i += 1
        return book

    def __len__(self):
        # it queries the database directly for an accurate, real-time count of total rows.
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM books")
        return cur.fetchone()[0]

    # ----------CREATING DATABASE ----------

    def create_tables(self):

        cur = self.conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS books(
            isbn INTEGER PRIMARY KEY,
            title VARCHAR ,
            author VARCHAR,
            genre VARCHAR,
            total INTEGER,
            available INTEGER
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS members(
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            email VARCHAR UNIQUE,
            join_date VARCHAR
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn VARCHAR,
            member_id INTEGER,
            issue_date VARCHAR,
            due_date VARCHAR,
            return_date VARCHAR,
            fine REAL DEFAULT 0
        )
        """)

        self.conn.commit()

    def load_books(self):

        self.books = []
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()

        for row in rows:
            self.books.append(Book(*row))


        # ---------- BOOK FUNCTIONS ---------- 

    def add_book(self):

        isbn = input("Enter ISBN: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")
        total = int(input("Enter Total Copies: "))

        try:
            self.conn.execute(
                "INSERT INTO books VALUES(?,?,?,?,?,?)",
                (isbn, title, author, genre, total, total)
            )

            self.conn.commit()
            print("Book Added Successfully!")

        except Exception as e:
            print("Book already exists.")

    def view_books(self):

        self.load_books()

        if len(self.books) == 0:
            print("\nNo books available.")
            return

        print("------ BOOK LIST ------")

        for i in self.books:
            print(i)

    def search_books(self):

        keyword = input("Enter title/author/genre: ")
        cur = self.conn.cursor()

        cur.execute("""
        SELECT *
        FROM books
        WHERE title LIKE ?
        OR author LIKE ?
        OR genre LIKE ?
        """,
        (f"%{keyword}%",
         f"%{keyword}%",
         f"%{keyword}%"))

        rows = cur.fetchall()

        if not rows:
            print("No matching books found.")
            return

        print("Search Results:")

        for i in rows:
            print(Book(*i))

    def remove_book(self):

        isbn = input("Enter ISBN to remove: ")
        cur = self.conn.cursor()
        cur.execute(
            "DELETE FROM books WHERE isbn=?",
            (isbn,)
        )

        self.conn.commit()

        if cur.rowcount > 0:
            print("Book Removed Successfully.")
        else:
            print("Book not found.")

    # ---------- MEMBER FUNCTIONS ---------- 

    def register_member(self):

        name = input("Enter Member Name: ")
        email = input("Enter Email: ")
        join_date = input("Enter Join Date (YYYY-MM-DD): ")

        try:

            self.conn.execute(
                """
                INSERT INTO members(name,email,join_date)
                VALUES(?,?,?)
                """,
                (name, email, join_date)
            )

            self.conn.commit()

            print("Member Registered Successfully!")

        except Exception as e :
            print("Email already exists.")

    def view_members(self):

        cur = self.conn.cursor()

        cur.execute("""
        SELECT member_id,name,email,join_date
        FROM members
        """)

        rows = cur.fetchall()

        if not rows:
            print("No members registered.")
            

        print("------ MEMBERS ------")

        for i in rows:

            member = Member(
                i[0],
                i[1],
                i[2],
                i[3],
                self
            )

            print(member)
            print("Borrowed Books:", member.borrowed_count)
            print()

            # ---------- ISSUE BOOK ---------- 

    def issue_book(self):

        isbn = input("Enter ISBN: ")
        member_id = int(input("Enter Member ID: "))
        issue_date = input("Issue Date (YYYY-MM-DD): ")
        due_date = input("Due Date (YYYY-MM-DD): ")

        cur = self.conn.cursor()

        # checking the book

        cur.execute(
            "SELECT available FROM books WHERE isbn=?",
            (isbn,)
        )

        book = cur.fetchone()

        if book is None:
            print("Book not found.")
            return

        if book[0] <= 0:
            print("Book is not available.")
            return

        # checking the member
        cur.execute(
            "SELECT * FROM members WHERE member_id=?",
            (member_id,)
        )

        if cur.fetchone() is None:
            print("Member not found.")
            return

        # inserting transaction

        cur.execute("""
        INSERT INTO transactions
        (isbn,member_id,issue_date,due_date)
        VALUES(?,?,?,?)
        """,
        (isbn, member_id, issue_date, due_date))

        # reducing available copies

        cur.execute("""
        UPDATE books
        SET available = available - 1
        WHERE isbn=?
        """, (isbn,))

        self.conn.commit()

        print("Book Issued Successfully!")

    # ---------- RETURN BOOK ---------- 

    def return_book(self):

        isbn = input("Enter ISBN: ")
        member_id = int(input("Enter Member ID: "))
        return_date = input("Return Date (YYYY-MM-DD): ")

        cur = self.conn.cursor()

        cur.execute("""
        SELECT id
        FROM transactions
        WHERE isbn=?
        AND member_id=?
        AND return_date IS NULL
        """,
        (isbn, member_id))

        row = cur.fetchone()

        if row is None:
            print("No issued record found.")
            return

        cur.execute("""
        UPDATE transactions
        SET return_date=?
        WHERE id=?
        """,
        (return_date, row[0]))

        cur.execute("""
        UPDATE books
        SET available = available + 1
        WHERE isbn=?
        """, (isbn,))

        self.conn.commit()

        print("Book Returned Successfully!")

    # ---------- CLOSE DATABASE ----------

    def close(self):
        self.conn.close()


#=================MAIN PROGRAM==================#

def main():     

    library = Library.from_database(DB)

    while True:

        print("========== LIBRARY MANAGEMENT ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Remove Book")
        print("5. Register Member")
        print("6. View Members")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. Total Books")
        print("10. Iterate Books")
        print("0. Exit")

        ch = input("Enter choice: ")

        if ch=="1":
            library.add_book()

        elif ch=="2":
            library.view_books()

        elif ch=="3":
            library.search_books()

        elif ch=="4":
            library.remove_book()

        elif ch=="5":
            library.register_member()

        elif ch=="6":
            library.view_members()

        elif ch=="7":
            library.issue_book()

        elif ch=="8":
            library.return_book()

        elif ch=="9":
            print("Total Unique Titles:", len(library))

        elif ch=="10":
            print("Books using Iterator: ")

            for i in library:
                print(i)

        elif ch=="0":
            library.close()
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
