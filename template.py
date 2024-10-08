import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
# to perform logging ( time , message)

# folder structure
list_of_files = [
    "src/__init__.py",
    # The __init__.py file inside your src folder is used to tell Python that the folder should be treated as a package
    # constructor file
    "src/helper.py",
    # helper for functionality
    "src/prompt.py",
    ".env",
    "setup.py", #t serves as the build script for the Python package and contains metadata about your project as well as instructions for how to install and distribute it.
    "app.py",
    "research/trials.ipynb",
   " test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    # so that it works on linux and mac and window
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")