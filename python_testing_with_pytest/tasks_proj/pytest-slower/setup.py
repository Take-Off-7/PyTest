from setuptools import setup


setup(
    name  = 'pytest-slower',
    version = '0.1.0',
    description = 'A pytest plugin to check and compare test duration',
    url = 'https://github.com/Take-Off-7/PyTest',
    author = 'TakeOff',
    author_email = 'tfakeye7@gmail.com',
    license = 'proprietary',
    py_modules = ['pytest_slower'],
    install_requires = ['pytest'],
    entry_points = {'pytest11': ['slower=pytest_slower',],},
)
