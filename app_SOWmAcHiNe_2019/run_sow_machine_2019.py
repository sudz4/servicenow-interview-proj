
import nbformat
from nbconvert import PythonExporter
from nbconvert.preprocessors import ExecutePreprocessor
import time

# List of your notebook files
notebooks = [
    "1_main.ipynb",
    "notebook2.ipynb",
    "notebook3.ipynb",
    "notebook4.ipynb",
    "notebook5.ipynb",
    "notebook6.ipynb"
]

# Delay times in seconds
delays = [10, 7, 6, 6, 5, 5]

# Execute the notebooks with specified delays
for i, notebook in enumerate(notebooks):
    print(f"Running {notebook}...")
    
    # Load the notebook
    with open(notebook) as f:
        nb = nbformat.read(f, as_version=4)
    
    # Execute the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': '.'}})
    
    # Save the executed notebook
    with open(notebook, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print(f"{notebook} completed.")
    
    # Wait for the specified delay before moving to the next notebook
    if i < len(delays):
        time.sleep(delays[i])

print("All notebooks have been executed.")
