# Type Hint

from typing import Optional, Union, Callable

# Optional [value] = int , None
# Union [value1, value2] = values 1, value 2
# Venv - Virtural Environment : Creates a custom sandbox for app to run.

type o_user = dict[str, str | int | None]

# Callable <- function returns a specific type of value

def create_user(first_name: str, last_name: str, age: int | None = None ) -> o_user:
    email = f"{first_name}_{last_name}@email.com"

    return {
        "first_name": first_name,
        "last_name" : last_name,
        "email" : email,
        "age": age,
    }

user1 = create_user("Amy",'Roy', 35)
print(user1)

mrk = int | None

def final_marks(roll_no: int, marks: mrk) -> str:
    return f"Roll No: {roll_no}, Marks: {marks}"

print(final_marks(1,88))
print(final_marks(2,None))