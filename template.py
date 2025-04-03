import os 
from pathlib import Path 
import logging  

# ✅ Fix Logging Format (Remove extra space in `format`)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [ 
    "src/__init__.py",  # ✅ Fixed "__init__.py" typo (was "_init__.py")
    "src/helper.py", 
    "src/prompt.py", 
    ".env", 
    "setup.py", 
    "app.py", 
    "research/trials.ipynb",
    "test.py"
]

# ✅ Fix Loop Indentation
for filepath in list_of_files: 
    filepath = Path(filepath)  # Convert to Path object
    filedir, filename = os.path.split(filepath)  

    if filedir:  # ✅ Fix condition (filedir != "") 
        os.makedirs(filedir, exist_ok=True)  
        logging.info("Creating directory: %s for the file: %s", filedir, filename)  

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:  
        with open(filepath, "w") as f:  
            pass  
        logging.info("Creating empty file: %s", filepath)  # ✅ Fix Indentation
    else:
        logging.info("%s already exists", filename)  # ✅ Fix Logging Format
