import os, logging
from pathlib import Path

# set up logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s : %(message)s]:')

list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'app.py',
    'setup.py',
    'research/trials.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filepath}.")

    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating an empty file: {filepath}.")

    else:
        logging.info(f"File: {filepath} already exists.")

        