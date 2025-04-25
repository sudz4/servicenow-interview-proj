import os
import glob
import papermill as pm
import re

# jupyter notebook directory
notebooks_dir = '/Users/sudz4/Desktop/TOOLS/servicenow-interview-proj/app_SOWmAcHiNe_2019'  # Replace with your directory path

# change pwd to the notebooks directory
os.chdir(notebooks_dir)

# retrieve all .ipynb files
notebook_files = glob.glob('*.ipynb')

# sort the notebooks by name
notebook_files.sort()

for nb in notebook_files:
    print(nb)


# execute notebooks sequentially
for idx, nb in enumerate(notebook_files, 1):
    print(f"\nExecuting notebook {idx}/{len(notebook_files)}: {nb}")
    try:
        pm.execute_notebook(
            input_path=nb,
            output_path=nb,  # overwrite option?
            parameters={},    # pas params if needed?
            progress_bar=True
        )
        print(f"Statement of Work (SOW) generated successfully {nb}")
    except Exception as e:
        print(f"Error executing {nb}: {e}")
        # ???? decide whether to continue or halt execution
        break  # use 'continue' to proceed with the next notebook despite the error ?