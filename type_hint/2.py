name: str = "Amit"
age: int = 38

# If we hv complicated dictionary with more information, this will become crowded.
# to resolve this we can use type alias.
# if we could pass dict[key, value]  <-- this will become easy to read and understand
# Option 1 : type User = dict[str, str | int | None]

type User = dict[str, str | int | None]

def create_user(first_name: str, last_name: str, age: int | None = None) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    
    return {
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "age" : age,
    }

user1 = create_user('Amy', "Roy", 20)
user2 = create_user('Shanta', "Roy", 35)

print(user1)
print(user2)
