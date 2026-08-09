name: str = "Amit"      # type casting as string
age: int = 38           # type casting as integer

#age = "20"          # error in tab - Problems in VS Code

#1.  def create_user(first_name: str, last_name: str, age: int = None):
# this will accept type cast value as per defined in variable

#2. def create_user(first_name: str, last_name: str, age: int = None) -> dict:
# Now we have type cast the output as dictionary, so we will accpt only dictionay type value

#3. Now if you check in Problem : getting error for age : int value only
# def create_user(first_name: str, last_name: str, age: int = None) -> dict:
# we only defined we want dictionary, but what will be key or value is missing. So to decide it we can write - 

#4. def create_user(first_name: str, last_name: str, age: int | None = None) -> dict[str, str | None | int]:
# adding value for key : values

def create_user(first_name: str, last_name: str, age: int | None = None) -> dict[str, str | None | int]:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    
    # this returns dictionary with info below
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
