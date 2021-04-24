from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'General functions for Python'
LONG_DESCRIPTION = 'General functions for Python: for work in both Python and in Notebooks!'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name='walpy', 
        version=VERSION,
        author='Walter Verwer',
        author_email='https://github.com/walterverwer/walpy',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['rpy2'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'walpy'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)