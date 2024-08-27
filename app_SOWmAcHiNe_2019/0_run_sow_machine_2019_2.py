import os
import nbformat
from nbconvert import PythonExporter
from nbconvert.preprocessors import ExecutePreprocessor
import time

def get_notebooks_from_path(path):
    """Retrieve all .ipynb files from the given directory."""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.ipynb')]

def run_notebooks(notebooks, delay_first_second):
    """Execute the notebooks with a delay between the first and second."""
    for i, notebook in enumerate(notebooks):
        print(f"Running {os.path.basename(notebook)}...")

        # Load the notebook
        with open(notebook) as f:
            nb = nbformat.read(f, as_version=4)

        # Execute the notebook
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': '.'}})

        # Save the executed notebook
        with open(notebook, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)

        print(f"{os.path.basename(notebook)} completed.")

        # Delay between the first and second notebook
        if i == 0:
            time.sleep(delay_first_second)

    print("All notebooks have been executed.")

if __name__ == "__main__":
    # PATH
    notebook_path = "/Users/sudz4/Desktop/SERVICENOW-INTERVIEW/servicenow-interview-proj/app_SOWmAcHiNe_2019"

    # RETRIEVE
    notebooks = get_notebooks_from_path(notebook_path)
    
    # SORT (1-6)
    notebooks.sort()

    # PRINT list of (ordered) notebooks
    print(notebooks)

    # DELAY (between 1st and 2nd notebook)
    delay_first_second = 10

    """RUN/EXECUTE"""
    run_notebooks(notebooks, delay_first_second)
