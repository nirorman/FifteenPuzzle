from setuptools import setup, find_packages

MAJOR_VERSION = '1'

setup(
    name='FifteenPuzzle',
    author='Nir Orman',
    author_email='nirorman@gmail.com',
    url='https://github.com/nirorman/FifteenPuzzle',
    version=MAJOR_VERSION,
    packages=find_packages(),
    scripts=['main.py'],
    install_requires=['texttable', 'click']
)
