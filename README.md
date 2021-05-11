# Readme walpy
Walpy is a general purpose package containing '30-second-functions'.

## Dependencies
Currently the package depends on: rpy2.


## Available functions:

### r_importer(modules, install_only=[], log=False)

_R to Python installer and importer. When importing R packages while working in a Python environment can lead to some unnecessary code. In order to provide an as clean and close to importing Python packages as possible importing experience, walpy has this function that allows one to import a list of R packages. The package is flexible enough to also allow for manual imports. If one wants to manually import an R package, simply specify the package(s) to be installed manually and map the example below the following code cell to the individual's use case._


### suppress(object)
_Use this function to suppress output. Simply use Python's 'with' function in combination with 'suppress()'._


### write_run(line, cell)
_This function is jupyter notebook specific. It allows the user to write and run a specific cell to a python (.py) script. Simply use %%write_run <file_name.py> at the top of the cell._
