from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(f:str)-> List[str]:
    '''

    :param f: file input
    :return: list of requirements
    '''
    req=[]
    with open(f) as file_obj:
        req=file_obj.readlines()
        req=[r.replace("\n","") for r in req]
    if HYPHEN_E_DOT in req:
        req.remove(HYPHEN_E_DOT)

    return req
setup(
    name= 'mlproject',
    version='0.0.1',
    author='Sharmi',
    author_email='sharmidevgupta@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')

)