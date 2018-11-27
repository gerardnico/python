# A Hello World Package

## About
This is a starting project that demonstrate how to create a [distribution package](https://gerardnico.com/lang/python/shipping/package) from a [regular package](https://gerardnico.com/lang/python/grammar/package)
  
## Project 

### Structure

This project use a [src layout](https://gerardnico.com/lang/python/shipping/project#structure)

```txt
├── src
│   └── mypackage
│       ├── __init__.py
│       └── mod1.py
├── setup.py
└── setup.cfg
```

that is declared in the [setup.py](setup.py) file

```python
packages=setuptools.find_packages(where='src'),
package_dir={'': 'src'},  # tell distutils packages are under src
```


  
### Installation
 
  * Get this (distribution package|project) locally
  * Install Python  
  * Install the setuptools
```dos
python -m pip install --upgrade pip setuptools wheel
```
  * Then 
```dos
cd directory/of/the/project
pip install .
```

### Console script 

This will install the `hello` [script](https://gerardnico.com/lang/python/engine/script) defines in the [setup.py](setup.py) file
at the `entry_points` property as the function `main` of the module [hello_cli](src/hello_nico/hello_cli.py)

```dos
where hello
```
```txt
C:\Python37-32\Scripts\hello.exe
```

  * Running the script
  
```dos
hello nico
```
```txt
>>> Arguments passed in: ['nico']
>>> Flags detected: <args []>
>>> Files detected: []
>>> NOT Files detected: <args ['nico']>
>>> Grouped Arguments: {'_': <args ['nico']>}
>>> Your IP: 143.176.206.81
```
  
### Dependencies

The dependencies are defined in the `install_requires` property of the [setup.py](setup.py) file.
  
## Documentation   

  * Code from the article [How to distribute a regular python package](https://gerardnico.com/lang/python/shipping/regular)
  * Mix between the [pipenv article](https://pipenv.readthedocs.io/en/latest/install/)




