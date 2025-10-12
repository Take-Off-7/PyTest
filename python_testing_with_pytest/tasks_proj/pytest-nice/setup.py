from setuptools import setup


setup(
    name  = 'pytest-nice',
    version = '0.1.0',
    description = 'A pytest plugin to turn FAILURE',
    url = 'https://github.com/Take-Off-7/PyTest',
    author = 'TakeOff',
    author_email = 'tfakeye7@gmail.com',
    license = 'proprietary',
    py_modules = ['pytest_nice'],
    install_requires = ['pytest'],
    entry_points = {'pytest11': ['nice=pytest_nice',],},
)
