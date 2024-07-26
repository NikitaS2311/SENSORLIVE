from setuptools import find_packages ,setup
# from typing import List
from typing import List

def get_requirements()->List[str]:

    reuirements_list :List[str] =[]

    return reuirements_list


setup (
name = 'sensor',
version= "0.1.1",
author="nikita",
author_email = "singh2002nikki@gmail.com",
packages = find_packages(),
install_requires = get_requirements(), #["pymongo"]

)