import os
import glob
import papermill as pm
import re

# Specify the directory containing your notebooks
notebooks_dir = '/Users/sudz4/Desktop/BOOK-II/servicenow-interview-proj/app_SOWmAcHiNe_2019'  # Replace with your directory path

# Change the current working directory to the notebooks directory
os.chdir(notebooks_dir)

# Retrieve all .ipynb files
notebook_files = glob.glob('*.ipynb')

# sort the notebooks by name
notebook_files.sort()

for nb in notebook_files:
    print(nb)


# Execute notebooks sequentially
for idx, nb in enumerate(notebook_files, 1):
    print(f"\nExecuting notebook {idx}/{len(notebook_files)}: {nb}")
    try:
        pm.execute_notebook(
            input_path=nb,
            output_path=nb,  # Overwrite the notebook with output; change if you want to keep the original unmodified
            parameters={},    # Pass parameters here if needed
            progress_bar=True
        )
        print(f"Successfully executed {nb}")
    except Exception as e:
        print(f"Error executing {nb}: {e}")
        # Decide whether to continue or halt execution
        break  # Use 'continue' if you want to proceed with the next notebook despite the error