from setuptools import setup

setup(
    name='guido',
    version='0.0.1',
    description='A simple cli tool for comparing contents of two paths (folders).',
    author='tomekzbrozek',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['guido'],
    install_requires=[],
    entry_points=
    '''
      [console_scripts]
      guido=guido:main
    ''',
)
