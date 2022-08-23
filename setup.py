from setuptools import setup, find_packages

setup(
    name='newpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/MariamMupa/newpackage',
    author='Mariam Mupa Mmbetsa',
    author_email='mupammbetsa2@gmail.com'
)
