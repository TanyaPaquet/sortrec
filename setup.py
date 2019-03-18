from setuptools import setup, find_packages

setup(
    name='sortrec',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Recursive calculations and sorting functions',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/TanyaPaquet/sortrec.git',
    author='Tanya Paquet',
    author_email='tanya.paquet@gmail.com'
)
