from setuptools import find_packages, setup  # Importing necessary functions from setuptools

from typing import List                      # Importing List type from typing module for type hinting



## Create a function which read the requirment.txt file and give a list of all requirments in cleaned format
def get_requirments(file_path:str)->List[str]:
    """ This function will return a list of all requirments """
    
    requirments = []
    with open(file_path) as f:
        requirments = f.readlines()                                   # Read all lines from the requirements file
        requirments = [req.replace("\n" ,"") for req in requirments]  # Remove newline characters
        
        if "-e ." in requirments:        # Check if '-e .' (editable install of current directory) is in requirements
            requirments.remove("-e .")   # Remove '-e .' from requirements list if present
    
    return requirments                 # Return the list of cleaned requirements


## Specifies metadata about your Python package (
setup(

    name = "machine Learning Project",                      # Name of the Python package
    version = "0.0.1",                                      # Version of the package
    author = "Gujuri Alekha",                               # Author's name
    author_email = "gujuri.alekha@gmail.com",               # Author's email address
    packages = find_packages(),                             # Automatically find all packages under the current directory
    install_requires = get_requirments("requirments.txt")   # Specify dependencies from requirements.txt

)
