from setuptools import find_packages,setup
from typing import List 


HYPHEN_EDOT = '-e .'


def get_requirements(file_path:str) -> List[str]:
    '''
    Return a list of requirements.txt 
    '''

    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.replace("/n","") for r in req ]
        if HYPHEN_EDOT in req:
            req.remove(HYPHEN_EDOT)
    

    return req

        


setup(
    name = "mlproject",
    version = '0.0.1',
    author = 'Arjun Ganesh',
    author_emal = 'avg3xt@virginia.edu',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'))



