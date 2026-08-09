# sample Code Quality — black, pylint, ruff, PEP8 Code

from typing import Union, Optional, Callable

student_score: Union[int, float] = 85.5

teacher_notes: Optional[str] = None

is_passing: Callable[[int], bool] = lambda score: score >= 40

test_keys = [35, 42, 50, 28]
passed_students = [score for score in test_keys if is_passing(score)]

'''
How to run the code
# 1. Create a virtual environment (we will name it 'myenv')
python -m venv myenv

# 2. Activate the virtual environment
source myenv/bin/activate   # Linux code

# 3. Install the tools using pip (while the environment is active)
pip install black pylint ruff

# 4. Run the tools on your Python files
black your_script.py
ruff check your_script.py
pylint your_script.py
'''