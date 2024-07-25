from setuptools import find_packages ,setup
# from typing import List
#from typing import 

def get_requirements()->list[str]:

    reuirements_list = list[str] =[]

    return reuirements_list


setup (
name = 'sensor',
version= "0.1.1",
author="nikita",
author_email = "singh2002nikki@gmail.com",
packages = find_packages(),
install_requires = get_requirements(), #["pymongo"]

)