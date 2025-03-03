import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

project_name = "textsummarizer"
list_files = [".github/workflows/.gitkeep",
              f"src/{project_name}/__init__.py",
              f"src/{project_name}/components/__init__.py",
              f"src/{project_name}/utils/__init__.py",
              f"src/{project_name}/utils/common.py",
              f"src/{project_name}/logging/__init__.py",
              f"src/{project_name}/config/__init__.py",
              f"src/{project_name}/config/configuration.py",
              f"src/{project_name}/pipeline/__init__.py",
              f"src/{project_name}/entity/__init__.py",
              f"src/{project_name}/constants/__init__.py",
              "config/config.yaml",
              "params.yaml",
              "main.py",
              "Dockerfile",
              "requirements.txt",
              "setup.py",
              "resarch/trails.ipynb",
              "test.py",]


for filepath in list_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    ## Check if filedirectory is not empty and create it if not
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directory if not exists
        logging.info(f"Created directory: {filedir} for the file '{filename}'")
        
    if (not os.path.exists(file_path)) or (os.path.isfile(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    
    else :
        logging.info(f"File already exists: {file_path}")