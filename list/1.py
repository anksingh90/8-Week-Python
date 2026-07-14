# Even Number Generator Write a generator function even_numbers(limit) that yields even numbers from 0 up to 
# (but not including) limit.

def even_numbers(limit):
    """Yield even numbers from 0 up to (but not including) limit."""
    for num in range(0, limit, 2):
        yield num

obj = even_numbers(10)

for number in obj:
    print(number)

