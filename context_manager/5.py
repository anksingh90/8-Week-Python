from contextlib import contextmanager
import time

@contextmanager
def timer(name="Operation"):
    """Simple timer context manager using @contextmanager."""
    start = time.time()
    print(f"▶ Starting {name}...")
    
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"⏱ {name} took {elapsed:.4f} seconds")

# Using it
with timer("Data Processing"):
    total = sum(range(1000000))

# Output:
# ▶ Starting Data Processing...
# ⏱ Data Processing took 0.0234 seconds