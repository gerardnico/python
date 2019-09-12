import io
import re

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with io.open('src/hello_nico/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

# Full Spec
# https://packaging.python.org/specifications/
setuptools.setup(

    # Mandatory
    #   * the name of your project (the archive name)
    # It must be free on the index PyPi
    name="hello-nico",
    #   * the version of your project (the archive version)
    version=version,

    # Packages to be added
    # See https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages
    # find_packages() takes a source directory and two lists of package name patterns to exclude and include.
    # If omitted, the source directory defaults to the same directory as the setup script.
    # Some projects use a src or lib directory as the root of their source tree,
    # and those projects would of course use "src" or "lib" as the first argument to find_packages().
    # (And such projects also need something like package_dir={'':'src'} in their setup() arguments,
    packages=setuptools.find_packages(where='src'),

    # SOURCEDIR
    package_dir={'': 'src'},  # tell distutils packages are under src

    # Script
    # https://packaging.python.org/specifications/entry-points/
    # scripts=[''],
    entry_points={
        'console_scripts': [
            'hello = hello_nico.hello_cli:main',
        ]
    },

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # Dependency declaration
    # A string or list of strings specifying what other distributions need to be installed when this one is.
    # See https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies
    install_requires=[
        'requests>=2.20.1',
        'clint>=0.5.1'
    ],

    tests_require=[
        'pytest==4.1.1',
    ],

    # Package data
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # Metadata to display on PyPI (https://pypi.org/)
    # See https://packaging.python.org/specifications/core-metadata/
    author="Nico",
    author_email="github@gerardnico.com",
    description="A small hello world package",
    license="PSF",
    keywords="hello world example examples",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gerardnico/python/",
    download_url="https://github.com/gerardnico/python/",
    project_urls={
        "Bug Tracker": "https://github.com/gerardnico/python/",
        "Documentation": "https://github.com/gerardnico/python/",
        "Source Code": "https://github.com/gerardnico/python/",
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    # could also include etc.

)
